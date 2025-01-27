#!/usr/bin/env python3
import csv
from typing import Set, Generator, Dict

def missing(source_path: str, legal_path: str, output_path: str) -> None:
    """
    Find rows in source CSV where AT_webuntisKurzname doesn't exist in Legal CSV's studentShortName.
    
    Args:
        source_path: Path to source CSV (semicolon-delimited)
        legal_path: Path to legal CSV (tab-delimited)
        output_path: Path for output CSV (semicolon-delimited)
    """
    # Get existing legal short names
    legal_names: Set[str] = set()
    with open(legal_path, 'r', encoding='utf-8') as legal_file:
        reader = csv.DictReader(legal_file, delimiter='\t')
        if 'studentShortName' not in reader.fieldnames:
            raise ValueError("Legal CSV missing studentShortName column")
            
        legal_names = {row['studentShortName'] for row in reader}

    # Process source file and write matches
    with open(source_path, 'r', encoding='utf-8') as source_file, \
         open(output_path, 'w', encoding='utf-8', newline='') as out_file:
        
        reader = csv.DictReader(source_file, delimiter=';')
        if 'AT_webuntisKurzname' not in reader.fieldnames:
            raise ValueError("Source CSV missing AT_webuntisKurzname column")
            
        writer = csv.DictWriter(out_file, fieldnames=reader.fieldnames, delimiter=';')
        writer.writeheader()
        
        for row in reader:
            if row['AT_webuntisKurzname'] not in legal_names:
                writer.writerow(row)

if __name__ == "__main__":
    # Example usage
    missing(
        source_path="00-Export20250103.csv",
        legal_path="LegalGuardian_20250124_0812.csv",
        output_path="missing.csv"
    )
