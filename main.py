import faust

app= faust.App('agents-demo')

greetings_topic = app.topic('greetings', value_type=str, value_serializer='raw')

# Consumer
@app.agent(greetings_topic)
async def greet(stream):
    async for greeting in stream:
        print(greeting)

# Producer
@app.timer(interval=1.0)
async def send_greeting():
    await greetings_topic.send(value='Hello, World!')
    
if __name__ == '__main__':
    app.main()
    