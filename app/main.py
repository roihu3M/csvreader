import tabulate
import argparse

from read_files import file_processing_func
from reports import Reports


reports_dict = {
    'student-performance' : Reports.student_performance
}

def parser_func():
    parser = argparse.ArgumentParser()
    parser.add_argument('--files', type=str, required=True, nargs='*')
    parser.add_argument('--report', type=str, required=True, choices=reports_dict.keys())
    args = parser.parse_args()
    return args

def main(argv=None):
    result_list = []
    args = parser_func()
    objects = file_processing_func(args.files)
    r = Reports()
    result_list = r.student_performance(objects)
    indices = list(range(1, len(result_list) + 1))
    print(tabulate.tabulate(result_list, headers="keys", showindex=indices))

if __name__ == "__main__":
     main()




    

            



        

            

