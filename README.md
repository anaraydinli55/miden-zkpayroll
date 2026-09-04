# Miden zkPayroll: Confidential Batch Payout Tool

A privacy-preserving batch payment engine built on Polygon Miden, enabling organizations and DAOs to distribute confidential salaries and token grants using Private P2ID Notes and client-side zero-knowledge proofs.

## Why Miden for Payroll?
On traditional EVM chains, all payroll transactions leak employee salary amounts and wallet addresses. 
With Polygon Miden Hybrid State & Actor Model:
- Confidential Balances: Transactions utilize private note types, exposing only note commitments on-chain.
- Client-Side Proving: Zero-knowledge proofs are generated locally on the senders device.
- Asynchronous Consumption: Recipients consume their notes asynchronously without race conditions or MEV front-running.

## Quickstart

### 1. Configure Payroll
Edit payroll.json with target addresses and token amounts.

### 2. Run Confidential Payout
python3 zkpayroll.py

### 3. Employee Claiming
Employees claim their private notes:
./claim_salary.sh

## Architecture
Employer CLI -> Generates Local ZK Proof (Client-side)
             -> Emits Private Note Commitment to Miden Network
Miden Testnet Node -> Verifies Proof (Zero Knowledge of Amount/Recipient)
Employee -> Syncs & Consumes Note via Nullifier

## License
MIT
