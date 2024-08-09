from chatApp import app, socketio, db

if __name__ == '__main__':
    # Create the schema (tables) if they don't already exist
    db.create_all()
    # Run the Flask application with SocketIO support
    socketio.run(app, debug=True)
