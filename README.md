Mathhack Registration Data Parser
===
## Data
* Data Folder `reg_data/`
    * -| `ori`   original PDF, folder indexed by reg id
    * -| `full`  organized PDF, named by reg id and name
    * -| `txt`  parsed txt file from PDF
    * -| `profile` personal data and unit gender
    * -| `purpose` purpose data

## Command Line Tools
### reg_pdf_generate.py
originaze original uploaded PDF file to `full` folder ,named by reg id and name
```
python reg_pdf_generate.py <registraion csv>
```

### reg_pdf_txt.py
parse pdf with [pdfminer/pdfminer.six](https://github.com/pdfminer/pdfminer.six)

parse all PDFs which under `full` folder to `txt`
```
python reg_pdf_txt.py
```
### txt_parse.py
parse personal data and purpose data from files in `txt`
```
python txt_parse.py personal
python txt_parse.py purpose
```
> some file need manual modified : 
> 4 5 21 41 48

### school_parse.py
summary of register's school data
```
python school_parse.py
```

