"""
    Author : Mridul Ahuja
    Github : https://github.com/mridah/csv2vcf
    Description : A small command line tool to convert CSV files to VCard files

"""

import os
import sys
import csv
import json

default_input_file_format = {
    'first_name': None,
    'last_name': None,
    'full_name': None,
    'nickname': None,
    'org': None,
    'tel': None,
    'url': None,
    'bday': None,
    'role': None,
    'email': None,
    'note': None
}


def convert_to_vcard(input_file, single_output, input_file_format):

    input_file_format = {**default_input_file_format, **input_file_format}

    FIRST_NAME = input_file_format['first_name']
    LAST_NAME = input_file_format['last_name']
    FULL_NAME = input_file_format['full_name']

    NICKNAME = input_file_format['nickname']

    ORG = input_file_format['org']
    TEL = input_file_format['tel']
    URL = input_file_format['url']
    BDAY = input_file_format['bday']
    ROLE = input_file_format['role']
    EMAIL = input_file_format['email']
    NOTE = input_file_format['note']

    # if single output option is selected
    if single_output :
        with open( input_file, 'r' ) as source_file:
            reader = csv.reader( source_file )
            single_vcf = open('csv2vcf/all_contacts.vcf', 'w')
            i = 0
            for row in reader:

                FN_VAL = row[FULL_NAME] if FULL_NAME is not None else ''
                FN_VAL = row[FIRST_NAME] + ' ' + \
                    row[LAST_NAME] if FN_VAL == '' else FN_VAL

                NICKNAME_VAL = row[NICKNAME] if NICKNAME is not None else ''
                ORG_VAL = row[ORG] if ORG is not None else ''
                TEL_VAL = row[TEL] if TEL is not None else ''
                URL_VAL = row[URL] if URL is not None else ''
                BDAY_VAL = row[BDAY] if BDAY is not None else ''
                ROLE_VAL = row[ROLE] if ROLE is not None else ''
                EMAIL_VAL = row[EMAIL] if EMAIL is not None else ''
                NOTE_VAL = row[NOTE] if NOTE is not None else ''

                print('BEGIN:VCARD')
                print('VERSION:3.0')
                print('N:' + FN_VAL)
                print('FN:' + FN_VAL)
                print('NICKNAME:' + NICKNAME_VAL)
                print('TEL;HOME;VOICE:' + TEL_VAL)
                print('EMAIL:' + EMAIL_VAL)
                print('BDAY:' + BDAY_VAL)
                print('ORG:' + ORG_VAL)
                print('ROLE:' + ROLE_VAL)
                print('URL:' + URL_VAL)
                print('NOTE:' + NOTE_VAL)
                print('END:VCARD')
                print('----------------------')

                # write the single file
                single_vcf.write( 'BEGIN:VCARD' + "\n")
                single_vcf.write( 'VERSION:3.0' + "\n")
                single_vcf.write( 'N:' + FN_VAL + ';' + "\n")
                single_vcf.write( 'FN:' + FN_VAL + "\n")
                single_vcf.write( 'NICKNAME:' + NICKNAME_VAL + "\n")
                single_vcf.write( 'TEL;HOME;VOICE:' + TEL_VAL + "\n")
                single_vcf.write( 'EMAIL:' + EMAIL_VAL + "\n")
                single_vcf.write( 'BDAY:' + BDAY_VAL + "\n")
                single_vcf.write( 'ORG:' + ORG_VAL + "\n")
                single_vcf.write( 'ROLE:' + ROLE_VAL + "\n")
                single_vcf.write( 'URL:' + URL_VAL + "\n")
                single_vcf.write( 'NOTE:' + NOTE_VAL + "\n")
                single_vcf.write( 'END:VCARD' + "\n")
                single_vcf.write( "\n")

                i += 1

            single_vcf.close()
            print(str(i) + " VCARDS written")
            print('----------------------')

    # default ( multi-file output )
    else :
        with open( input_file, 'r' ) as source_file:
            reader = csv.reader( source_file )
            i = 0
            for row in reader:

                FN_VAL = row[FULL_NAME] if FULL_NAME is not None else ''
                FN_VAL = row[FIRST_NAME] + ' ' + \
                    row[LAST_NAME] if FN_VAL == '' else FN_VAL

                NICKNAME_VAL = row[NICKNAME] if NICKNAME is not None else ''
                ORG_VAL = row[ORG] if ORG is not None else ''
                TEL_VAL = row[TEL] if TEL is not None else ''
                URL_VAL = row[URL] if URL is not None else ''
                BDAY_VAL = row[BDAY] if BDAY is not None else ''
                ROLE_VAL = row[ROLE] if ROLE is not None else ''
                EMAIL_VAL = row[EMAIL] if EMAIL is not None else ''
                NOTE_VAL = row[NOTE] if NOTE is not None else ''

                print('BEGIN:VCARD')
                print('VERSION:3.0')
                print('N:' + FN_VAL)
                print('FN:' + FN_VAL)
                print('NICKNAME:' + NICKNAME_VAL)
                print('TEL;HOME;VOICE:' + TEL_VAL)
                print('EMAIL:' + EMAIL_VAL)
                print('BDAY:' + BDAY_VAL)
                print('ORG:' + ORG_VAL)
                print('ROLE:' + ROLE_VAL)
                print('URL:' + URL_VAL)
                print('NOTE:' + NOTE_VAL)
                print('END:VCARD')
                print('----------------------')

                # write each entry
                each_vcf = open('csv2vcf/' + FN_VAL + '_' + TEL_VAL + ".vcf", 'w')
                each_vcf.write( 'BEGIN:VCARD' + "\n")
                each_vcf.write( 'VERSION:3.0' + "\n")
                each_vcf.write( 'N:' + FN_VAL + ';' + "\n")
                each_vcf.write( 'FN:' + FN_VAL + "\n")
                each_vcf.write( 'NICKNAME:' + NICKNAME_VAL + "\n")
                each_vcf.write( 'TEL;HOME;VOICE:' + TEL_VAL + "\n")
                each_vcf.write( 'EMAIL:' + EMAIL_VAL + "\n")
                each_vcf.write( 'BDAY:' + BDAY_VAL + "\n")
                each_vcf.write( 'ORG:' + ORG_VAL + "\n")
                each_vcf.write( 'ROLE:' + ROLE_VAL + "\n")
                each_vcf.write( 'URL:' + URL_VAL + "\n")
                each_vcf.write( 'NOTE:' + NOTE_VAL + "\n")
                each_vcf.write( 'END:VCARD' + "\n")
                each_vcf.write("\n")
                each_vcf.close()

                i += 1

            print(str(i) + " VCARDS written")
            print('----------------------')


def main(args):
    args_len = len(args)

    if args_len < 3 or args_len > 4 :
        print ( "Usage:")
        print ( args[0] + " filename")
        sys.exit()

    if args_len == 3 :
        input_file = args[1]
        
        try :
            input_file_format = json.loads(args[2])
        except Exception as e :
            print('\033[91m'+"ERROR : json could not be parsed"+'\033[0m')
            sys.exit()

        single_output = 0
    elif args_len == 4 :
        input_file = args[1]

        if args[2] == '-s' or args[2] == '--single' :
            single_output = 1
        else :
            print('\033[91m'+"ERROR : invalid argument `" + args[2] + "`"+'\033[0m')
            sys.exit()

        try :
            input_file_format = json.loads(args[3])
        except Exception as e :
            print('\033[91m'+"ERROR : json could not be parsed"+'\033[0m')
            sys.exit()

    if not os.path.exists(input_file) :
        print('\033[91m'+"ERROR : file `" + input_file + "` not found"+'\033[0m')
        sys.exit()

    if not os.path.exists('csv2vcf') :
        os.makedirs('csv2vcf')

    convert_to_vcard(input_file, single_output, input_file_format)

if __name__ == '__main__':
    main(sys.argv)
