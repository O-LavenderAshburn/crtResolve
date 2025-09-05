```
                             ___  
                            //   ) )                                               
    ___      **    **  ___ //___/ /   ___      ___      ___     //          ___    
  //   ) ) //  ) )  / /   / ___ (   //___) ) ((   ) ) //   ) ) // ||  / / //___) ) 
///       //       / /   //   | |  //         \ \    //   / / //  || / / //
((____   //       / /   //    | | ((____   //___) ) ((___/ / //   ||/ / ((____  
```

A Python tool for discovering and resolving subdomains using crt.sh certificate transparency logs.


- Fetch subdomains directly from crt.sh for a given domain/TLD.
- Parse existing CSV files of subdomains.
- Resolve subdomains to IP addresses.

Basic Usage
- `python3 <input_file.csv>` — CSV file of subdomains (optional if using --tld)

 Options
- `--tld <domain> [output-file]` — Fetch subdomains for a given domain/TLD directly from crt.sh`
- ` --count <N> `— Stop after resolving N subdomains
- `--out_filename <name>` — Base name for output file (default: resolved_subdomains)`
