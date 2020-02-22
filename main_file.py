import wikipedia
import wolframalpha

print("Hi there, how may I help you?")
query_type = str(input("a. for math or science related questions - 1\nb. for general topics - 2\n>"))
my_input = str(input("question: "))

if query_type == '1':
    #wolframalpha
    app_id = "Wolfram Alpha App ID"
    client = wolframalpha.Client(app_id)
    res = client.query(my_input)
    answer = next(res.results).text
    print(answer)
        
elif query_type == '2':
    #wikipedia
    print(wikipedia.summary(my_input))
