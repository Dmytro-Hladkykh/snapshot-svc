# NFT Snapshot Service

This service creates a snapshot of NFT collection owners.

## Setup and Run

1. Clone the repository and navigate to the project directory.

2. Set up a virtual environment:

```
python -m venv venv
source venv/bin/activate  # For Unix or MacOS
venv\Scripts\activate  # For Windows
```

3. Install dependencies:

```
pip install -r requirements.txt
```

4. Create a `.env` file in the root directory with:

```
WEB3_PROVIDER_URL=https://your-provider-url.com
NFT_COLLECTION_ADDRESS=0xYourContractAddressHere
```

5. Ensure `ABI.json` with the contract ABI is in the `contracts` folder.

6. Run the script:

```
python snapshot.py
```

Results will be saved in `snapshot.json`.
