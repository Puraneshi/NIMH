import requests
import json
import time
import gzip

pmids = []
with open('pmid.txt', 'r') as file:
    for line in file:
        pmids.append(line.strip())
print(f'{len(pmids)} pmids, {len(set(pmids))} unique ids')

api_url = "https://api.openalex.org/works/pmid:{}"
jsonOutput_file = "openalex-snapshot/data/works/calls.jsonl.gz"
failed_file = "failed_calls.txt"

headers = {'User-Agent': 'mailto:rsnd.leo@gmail.com'}

failed_calls = []
max_retries = 3

with gzip.open(jsonOutput_file, 'w') as outfile, open(failed_file, 'w') as failed_calls_file:
    for id in set(pmids):
        retries = 0
        time.sleep(0.1)
        while retries < max_retries:
            response = requests.get(api_url.format(id), headers=headers)
            if response.status_code == 200:
                json_data = response.json()
                json_line = json.dumps(json_data) + '\n'
                outfile.write(json_line.encode('utf-8'))
                break
            else:
                print(f"Failed to fetch data for {id}. Retrying...")
                retries += 1
                time.sleep(1)  # Wait before retrying

        if retries == max_retries:
            print(f"Failed to fetch data for {id} after {max_retries} retries.")
            failed_calls_file.write(id + '\n')
            failed_calls.append(id)


print(f"Process completed. Check {failed_file} for pending calls.")
