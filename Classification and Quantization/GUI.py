import os
import cv2
from datetime import datetime
import PySimpleGUI as sg

sg.theme('dark grey 9')
# Define the window's contents
layout = [
    [sg.T("")], [sg.Text("Choose a video file: "), sg.Input(), sg.FileBrowse(key="-VIDEO_IN-"), sg.Button('Open Video')],
    [sg.T("")], [sg.Text("Choose a Folder: "), sg.Input(), sg.FolderBrowse(key="-IMAGE_IN-"), sg.Button('Open Image')],
    [sg.Image(key="-IMAGE_OUT-", size=(500, 500)), sg.Button('Best'), sg.Button('Not Best'), sg.Button('Skip Frame'),
     sg.Button('Quit'), sg.Text(size=(40, 3), key='-OUTPUT-', font=('Arial', 15))],
    [sg.Button('Exit')], ]

# Create the window
window = sg.Window('Window Title', layout, size=(1100, 700))

while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break
    elif event == "Open Video":
        window["-OUTPUT-"].update("")
        cap = cv2.VideoCapture(values["-VIDEO_IN-"])
        nframes = 0
        while cap.isOpened():
            success, frame = cap.read()
            if not success:
                window["-OUTPUT-"].update("Video Finished\nChoose another Video\nOR Click Exit", text_color="yellow")
                break  # Exit at the end of the video
            if nframes % 20 == 0:  # Skipping every 5 frames
                resized_frame = cv2.resize(frame, (500, 500))
                imgbytes = cv2.imencode('.png', resized_frame)[1].tobytes()  # Image to Byte
                window["-IMAGE_OUT-"].update(data=imgbytes)
                window.refresh()
                event2, values2 = window.read()
                if event2 == 'Best':
                    os.makedirs('Best', exist_ok=True)
                    cv2.imwrite(f'Best/{str(datetime.now().strftime("%d-%m-%Y_%H-%M-%S"))}.png', frame)
                elif event2 == "Not Best":
                    os.makedirs('Not Best', exist_ok=True)
                    cv2.imwrite(f'Not Best/{str(datetime.now().strftime("%d-%m-%Y_%H-%M-%S"))}.png', frame)
                elif event2 == 'Skip Frame':
                    pass
                elif event2 == "Quit" or event2 == sg.WINDOW_CLOSED or event2 == 'Exit':
                    window.close()
            nframes += 1

        cap.release()

    elif event == 'Open Image':
        for filename in os.scandir(values['-IMAGE_IN-']):
            if filename.is_file():
                print(filename.name)
                frame = cv2.imread(filename.path)
                resized_frame = cv2.resize(frame, (500, 500))
                imgbytes = cv2.imencode('.png', resized_frame)[1].tobytes()  # Image to Byte
                window["-IMAGE_OUT-"].update(data=imgbytes)
                window.refresh()
                event2, values2 = window.read()
                if event2 == 'Best':
                    os.makedirs('Best', exist_ok=True)
                    cv2.imwrite(f'Best/{str(datetime.now().strftime("%d-%m-%Y_%H-%M-%S"))}.png', frame)
                elif event2 == "Not Best":
                    os.makedirs('Not Best', exist_ok=True)
                    cv2.imwrite(f'Not Best/{str(datetime.now().strftime("%d-%m-%Y_%H-%M-%S"))}.png', frame)
                elif event2 == 'Skip Frame':
                    pass
                elif event2 == "Quit" or event2 == sg.WINDOW_CLOSED or event2 == 'Exit':
                    window.close()
    # Output a message to the window
    # window['-OUTPUT-'].update('Hello ' + values['-INPUT-'] + "! Thanks for trying PySimpleGUI")

# Finish up by removing from the screen
window.close()
