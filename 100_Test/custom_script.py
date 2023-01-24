
import joblib
import argparse
from CustomtestModel import CustomtestModel

def main(inputfile):
    model = CustomtestModel(inputfile = inputfile)
    response = model.getjson()
    model_file_name = 'test_custom_model'
    joblib.dump(response, model_file_name)
    
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--inuptfilepath", type=str, default="testdata.xlsx")
    args = parser.parse_args()
    main(inputfile=args.inuptfilepath)    
