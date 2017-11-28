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
organize original uploaded PDF file to `full` folder, named by reg id and name
```
python reg_pdf_generate.py [file]
```

### reg_pdf_txt.py
parse pdf with [pdfminer/pdfminer.six](https://github.com/pdfminer/pdfminer.six)

parse all PDFs which under `full` folder to `txt`
```
python reg_pdf_txt.py [--update]
```
### txt_parse.py
parse personal data and purpose data from files in `txt`
```
python txt_parse.py profile [--update]
python txt_parse.py purpose [--update]
```
> some file need manual modified : 
> copy from `old/profile`

### summary_parse.py
summary of register's data
```
python summary_parse.py profile
python summary_parse.py gender
python summary_parse.py school
```

### textrank.py
textrank of each register's purpose
```
python textrank.py
```

### csv2json.py
> modified from [maur1th/csv2json-fixture](https://github.com/maur1th/csv2json-fixture)
> 
generate Django model's fixtures
* default setting : auto increment for primary key
* `--pk` option : use first column as primary key

```
python csv2json.py file.csv app.Model [--pk]
```