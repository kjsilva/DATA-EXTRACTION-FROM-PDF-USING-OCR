#import the main class using the help of __init__.py
from utils.mainClass import PdfExtractor
from utils.lib import traceback, file_id
from utils.paths import INPUT_DIR, OUTPUT_DIR, log_error_txt

#main program
def main(input_pdf, outputpath):
    try:
        print('Running the OCR program......')
        #initialize the class
        pdf_text_extractor = PdfExtractor()

        #extracting 
        pdf_text_extractor.text_extractor(input_pdf, outputpath)
        print(f'Successfully run..........\nSaved to output path')
    except Exception as e:
        #log error 
        with open(log_error_txt, 'a', encoding='utf-8') as f:
            f.write(f'\n[{file_id}] ERROR: {str(e)}\n')
            f.write(traceback.format_exc())

#running the program
if __name__ == '__main__':
    pass
    #input pdf file
    data_path = INPUT_DIR / 'input.pdf'
    output_path = OUTPUT_DIR 
    #run the program
    main(data_path, output_path)




