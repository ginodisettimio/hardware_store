import uvicorn

if __name__ == '__main__':
    # No me deja poner el host='0.0.0.0'
    uvicorn.run('server.app:hardware', port=8000, reload=True)
