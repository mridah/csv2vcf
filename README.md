# csv2vcf
csv2vcf is a small command line tool to convert CSV files to VCard (.vcf) files.

## Usage :

Go to terminal or command prompt and type :

```
python csv2vcf.py CSV_FILE_NAME [ -s | --single ] INPUT_FILE_FORMAT
```

Where :

- `CSV_FILE_NAME` is the full name of the CSV file you want to convert
- `INPUT_FILE_FORMAT` is a JSON formatted string which tells **csv2vcf** how to parse your input file
- `-s` or `--single` : use this argument if you want your output in a single file. Optional parameter. By default, the program will create separate Vcard files for each entry



###### JSON Format :

The JSON string can have the following keys :

`name`, `nickname`, `org`, `tel`, `url`, `bday`, `role`, and `email`, where each property is in accordance with [vCard property types](https://en.wikipedia.org/wiki/VCard)

Format is `{KEY_1:KEY_1_COLUMN_NO, KEY_2:KEY_2_COLUMN_NO, ...}`


###### Example :

Suppose you have a CSV file `contacts.csv` with the following content :

```
+-----------+-------------+
|    NAME   |    MOBILE   |
+-----------+-------------+
|   Mrid    |  1111111111 |
|   Arnav   |  2222222222 |
|   Sunil   |  3333333333 |
|     .     |      .      |
|     .     |      .      |
|     .     |      .      |
+-----------+-------------+
```

To convert this file to vCard, you will have to write :

`python csv2vcf.py contacts.csv '{"name":1, "tel":2}'`

if you want separate vCards for each person, or

`python csv2vcf.py -s contacts.csv '{"name":1, "tel":2}'`

if you want to generate a single vCard file


## Report bugs and suggestions :
If you want to report a bug or want to add a sugestion, just add it in the issues. Or you can mail me at [this](mailto:mridul.ahuja@gmail.com).


## Copyright and license :

The license is available within the repository in the [LICENSE](https://github.com/mridah/csv2vcf/blob/master/LICENSE.md) file.
