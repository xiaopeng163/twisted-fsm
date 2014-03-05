### Write TCP/UDP communication Program with Finite State Machine


what is FSM, please see Wikipedia http://en.wikipedia.org/wiki/Finite-state_machine


### how to use this template


If you want to write TCP program to connect to server with retry timer, or other timers, FSM, you can use this template.

├── constants.py
├── factory.py
├── fsm.py
├── main.py
├── protocol.py
├── README.md
├── requirements.txt
└── timer.py

`main.py` is where the program start.

Modify `fsm.py` to add more state.(now it only has two state: True means TCP connected, False means not) Through FSM to control factory and protocol.

Modify `factory.py` to add more TCP action.

Modify `protocol.py` to add more action when TCP is connected, message is sending or receiveing from this TCP connection.


demo usage::

    penxiao@ubuntu:~/Demo/twisted_fsm_template$ python main.py -h
    usage: main.py [-h] -r REMOTE_IP -l LOCAL_IP -p REMOTE_PORT

    This is a demo twsited FSM framework

    optional arguments:
      -h, --help            show this help message and exit
      -r REMOTE_IP, --remote_ip REMOTE_IP
                            The remote ip address
      -l LOCAL_IP, --local_ip LOCAL_IP
                            The local ip address
      -p REMOTE_PORT, --remote_port REMOTE_PORT
                            the remote server port
    penxiao@ubuntu:~/PycharmProjects/twisted_fsm_template$