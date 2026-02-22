#!/usr/bin/env python3
import ast
import json
import os
import re
import sys
import time
from pathlib import Path
from urllib import request
from urllib import error as urlerror

API_URL = "https://solodit.cyfrin.io/api/v1/solodit/findings"


def parse_useful_tags(path: Path):
    text = path.read_text(encoding="utf-8")
    m = re.search(r"useful_tags\s*=\s*(\[.*?\])\s*\n\n", text, re.S)
    if not m:
        m = re.search(r"useful_tags\s*=\s*(\[.*\])", text, re.S)
    if not m:
        raise ValueError("Could not parse useful_tags from file")
    tags = ast.literal_eval(m.group(1))
    return set(tags)


def post_json(url: str, api_key: str, payload: dict):
    body = json.dumps(payload).encode("utf-8")
    req = request.Request(url, data=body, method="POST")
    req.add_header("Content-Type", "application/json")
    req.add_header("X-Cyfrin-API-Key", api_key)
    with request.urlopen(req, timeout=60) as resp:
        return json.loads(resp.read().decode("utf-8"))


def finding_tags(f):
    tags = []
    scored = f.get("issues_issuetagscore")
    if isinstance(scored, list):
        for item in scored:
            if not isinstance(item, dict):
                continue
            tag_obj = item.get("tags_tag")
            if isinstance(tag_obj, dict):
                title = tag_obj.get("title")
                if isinstance(title, str) and title.strip():
                    tags.append(title.strip())
    if tags:
        return tags

    results = []
    for key in ("category", "kind", "impact"):
        v = f.get(key)
        if isinstance(v, str) and v.strip():
            results.append(v.strip())
    return results


def main():
    if len(sys.argv) != 5:
        print("Usage: fetch_solodit_sample.py <api_key> <useful_tags_path> <output_path> <sample_size>")
        sys.exit(2)

    api_key = sys.argv[1].strip()
    useful_tags_path = Path(sys.argv[2])
    output_path = Path(sys.argv[3])
    sample_size = int(sys.argv[4])

    useful_tags = parse_useful_tags(useful_tags_path)

    matched = []
    page = 1
    page_size = 100
    seen_ids = set()

    while len(matched) < sample_size and page <= 400:
        payload = {
            "page": page,
            "pageSize": page_size,
            "filters": {},
        }
        try:
            data = post_json(API_URL, api_key, payload)
        except urlerror.HTTPError as e:
            if e.code == 429:
                retry_after = e.headers.get("Retry-After")
                wait_s = int(retry_after) if retry_after and retry_after.isdigit() else 65
                time.sleep(wait_s)
                continue
            raise
        findings = data.get("findings", []) or []
        if not findings:
            break

        for f in findings:
            fid = str(f.get("id", ""))
            if not fid or fid in seen_ids:
                continue
            seen_ids.add(fid)

            tags = finding_tags(f)
            hit_tags = [t for t in tags if t in useful_tags]
            if not hit_tags:
                continue

            matched.append(
                {
                    "id": fid,
                    "title": f.get("title", ""),
                    "impact": f.get("impact", ""),
                    "protocol_id": f.get("protocol_id", ""),
                    "auditfirm_id": f.get("auditfirm_id", ""),
                    "kind": f.get("kind", ""),
                    "tags": tags,
                    "matched_useful_tags": hit_tags,
                }
            )
            if len(matched) >= sample_size:
                break

        page += 1
        time.sleep(0.3)

    output = {
        "sample_size": len(matched),
        "requested_size": sample_size,
        "api_url": API_URL,
        "matched_findings": matched,
    }
    output_path.write_text(json.dumps(output, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"Saved {len(matched)} findings to {output_path}")


if __name__ == "__main__":
    main()
