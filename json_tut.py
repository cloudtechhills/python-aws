import json

# This uses a json string as an input 

json_string = """
{
    "Input":[
        {
        "Text":"I am learning to code in AWS",
        "SourceLanguageCode":"en",
        "TargetLanguageCode":"fr",
        "Required": true
        }
    ]
}
"""
### json.load() & json.dump() - Use to input and output JSON from files and into files.
### json.loads() & json.dumps() - Use to input and outputting JSON from strings and into strings.


def main():
    # json_input = json.loads(json_string)
    # print(json_input)


    # json_input = json.loads(json_string)
    # indented_format = json.dumps(json_input, indent=2)
    # print(indented_format)


    json_input = json.loads(json_string)
    text = json_input['Input'][0]['Text']
    source_language_code = json_input['Input'][0]['SourceLanguageCode']
    target_language_code = json_input['Input'][0]['TargetLanguageCode']
    print(text, source_language_code, target_language_code)

    
if __name__=="__main__":
    main()
