import socketio
import uvicorn
from models import Riddle, Player, riddles
from random import sample

sio = socketio.AsyncServer(async_mode='asgi', cors_allowed_origins='*')

app = socketio.ASGIApp(sio)


@sio.event
async def connect(sid, data):
    random_riddles: list[Riddle] = sample(riddles, 5)
    player: Player = Player(name=sid, score=0, current_index=0, count=1, riddles=random_riddles)
    await sio.save_session(sid, player)


@sio.on('next')
async def next(sid, data):
    try:
        res: Player = await sio.get_session(sid)
        await sio.emit('riddle', to=sid, data={'text': res.riddles[res.current_index].text, 'number': res.count})
        res.riddle = res.riddles[res.current_index].text
        await sio.save_session(sid=sid, session=res)
    except IndexError:
        await sio.emit('over', {}, to=sid)


@sio.on('answer')
async def answer(sid, data):
    user: Player = await sio.get_session(sid)
    text = data['text'].split(' ')[0] if ' ' in data['text'] else data['text']
    if text.lower() == user.riddles[user.current_index].answer:
        user.score += 1
        await sio.emit('score', to=sid, data={'value': user.score})
        await sio.emit('result', to=sid, data={'text': user.riddles[user.current_index].text, 'is_correct': True,
                                'answer': user.riddles[user.current_index].answer, 'number': user.count})
        user.current_index += 1
        user.count += 1
    else:
        await sio.emit('over_game', {}, to=sid)

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
