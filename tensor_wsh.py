import six
import tf # When testing is done, uncomment

_GOODBYE_MESSAGE = u'Goodbye'

def web_socket_do_extra_handshake(request): #ignore, assuming unneeded.
    pass

def web_socket_transfer_data(request): # change here.
    while True:
        line = request.ws_stream.receive_message()
        if line is None:
            return
        if isinstance(line, six.text_type): # edit this function to include python calls
            text = []
            text.append(line)
            final = str(tf.cyb(text))
            request.ws_stream.send_message(final, binary=False) # this line should return the result of the classification
            if line == _GOODBYE_MESSAGE:
                return
        else:
            request.ws_stream.send_message(line, binary=True)


# vi:sts=4 sw=4 et
