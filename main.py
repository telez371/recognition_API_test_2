from mindee import Client, documents

my_api_key = "136c2ea857c5a00b8e58e63a0a5c8fa6"
mindee_client = Client(api_key=my_api_key)


def text_recognition(file_path, text_file_name="result.txt"):
    input_doc = mindee_client.doc_from_path(file_path)
    api_response = input_doc.parse(documents.TypeReceiptV4)
    print(api_response.document)

    with open(text_file_name, "w") as file:
        file.write(f"{api_response.document}\n")

    return f"Result write into {text_file_name}"


def main():
    my_check = input("Load a file from disk: ")
    print(text_recognition(file_path=my_check))


if __name__ == '__main__':
    main()
