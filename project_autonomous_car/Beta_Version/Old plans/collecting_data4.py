import numpy as np
import cv2
import serial
import pygame
from pygame.locals import *
import socket
import time
import os
X = np.empty((0, self.input_size))
y = np.empty((0, 4))
                            # simple orders
if key_input[pygame.K_UP]:

if key_input[pygame.K_DOWN]:

if key_input[pygame.K_RIGHT]:

if key_input[pygame.K_LEFT]:

if key_input[pygame.K_x] or key_input[pygame.K_q]:
    
elif event.type == pygame.KEYUP:
                            self.ser.write(chr(0).encode())

                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break

            # save data as a numpy file
            file_name = str(int(time.time()))
            directory = "training_data"
            if not os.path.exists(directory):
                os.makedirs(directory)
            try:
                np.savez(directory + '/' + file_name + '.npz', train=X, train_labels=y)
            except IOError as e:
                print(e)

            end = cv2.getTickCount()
            # calculate streaming duration
            print("Streaming duration: , %.2fs" % ((end - start) / cv2.getTickFrequency()))

            print(X.shape)
            print(y.shape)
            print("Total frame: ", total_frame)
            print("Saved frame: ", saved_frame)
            print("Dropped frame: ", total_frame - saved_frame)

        finally:
            self.connection.close()
            self.server_socket.close()
