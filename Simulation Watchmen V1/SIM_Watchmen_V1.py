import pyautogui
import keyboard
import time 
import PIL
import numpy as np
from mss import mss
from datetime import datetime
from PIL import ImageGrab
import os
import ctypes
from wakepy import keep
import sys





#####     @py.exe S:\CAD_Office\Muhsin\NXOPEN\Simulation_Watchmen_V1\SIM_Watchmen_V1.py %*

##_" + username + "_" + date_time +"

def main() :




    with keep.presenting():

        username = str(os.getlogin())
        username = username.replace(".", "")
        #### IMAGE PATHS AND WELCOME MESSAGE
        print("Simulation watch has begun!")

        image_path = "S:\\CAD_Office\\Muhsin\\NXOPEN\\Simulation_Watchmen_V1\\Collision_Pop_Up.png"
        
        def capture_collision(image_path):
            ####### PLACE TO SAVE COLLISION IMAGES
            with open("S:\\CAD_Office\\Muhsin\\NXOPEN\\Simulation_Watchmen_V1\\DATA\\FILEPATH-" + username +".TXT", 'r') as PATHFILE:
                path = PATHFILE.read()
            
            now = datetime.now() # current date and time

            date_time = now.strftime("%d%m_%H%M")            
            #print(path)
            if not os.path.exists(path + "\\SimulationData_" + str(date_time) + "\\Collision_Screenshots"):
                os.makedirs(path + "\\SimulationData_" + str(date_time) + "\\Collision_Screenshots")
            lst = os.listdir(path + "\\SimulationData_" + str(date_time) + "\\Collision_Screenshots")
            if not os.path.exists(path + "\\SimulationData_" + str(date_time) + "\\ToolPathTime"):
                os.makedirs(path + "\\SimulationData_" + str(date_time) + "\\ToolPathTime")
            lst1 = os.listdir(path + "\\SimulationData_" + str(date_time) + "\\ToolPathTime")
            
            now = datetime.now() # current date and time

            date_time = now.strftime("%d%m_%H%M")
            
            
            text_file = open(path + "\\SimulationData_" + str(date_time) + "\\ToolPathTime\\OperationTimeData_" + username + "_" + date_time + ".txt", "w")
            currentDateAndTime = datetime.now()
            text_file.write("Simulation started -" + str(currentDateAndTime))
            number_of_screenshots = len(lst)
            program_number = len(lst1)
            screenshot_2 = pyautogui.screenshot(region=(700,60, 140, 90))
            screenshot_2.save("S:\\CAD_Office\\Muhsin\\NXOPEN\\Simulation_Watchmen_V1\\TIMER_CHECK_DATA\\Timer2-" + username +".png")
            img2 = np.array(screenshot_2)
            #### WHILE LOOP TO LOOK AT THE SCREEN AND EXECUTE
            while True:
                ### TAKE PROGRAM SCREENSHOT TO COMPARE LATER
                program_screenshot1 = pyautogui.screenshot(region=(75,200, 420, 850))
                program_screenshot4 = pyautogui.screenshot(region=(0,0, 520, 1100))
                
                ps_array1 = np.array(program_screenshot1)
                time.sleep(1)
                
                
                
                
                with open("S:\\CAD_Office\\Muhsin\\NXOPEN\\Simulation_Watchmen_V1\\SIM_CONTROL_DATA\\SIM_CONTROL-" + username + ".txt") as file:
                    lines = [line.rstrip() for line in file]
                    if 'STOP SIMULATION' in lines:

                        print("User Abort. Watchmen terminated!")
                        time.sleep(3)
                        currentDateAndTime = datetime.now()
                        text_file.write("\nSimulation watch terminated by user, Time: "+ str(currentDateAndTime) + ", Number of Collisions:  "+ str(number_of_screenshots))
                        text_file.close()
                        break
                        sys.exit()

                screenshot_1 = pyautogui.screenshot(region=(180,60, 140, 90))
                screenshot_1.save("S:\\CAD_Office\\Muhsin\\NXOPEN\\Simulation_Watchmen_V1\\TIMER_CHECK_DATA\\Timer1-" + username +".png")
                img1 = np.array(screenshot_1)
            #### MANUAL EXIT CODE    
                if keyboard.is_pressed('q'):
                    print("User Abort. Watchmen terminated!")
                    currentDateAndTime = datetime.now()
                    text_file.write("\nSimulation watch terminated by user, Time: "+ str(currentDateAndTime) + ", Number of Collisions:  "+ str(number_of_screenshots))
                    text_file.close()
                    break
                    sys.exit()
            #### TIMER CHECK EXIT     
                if np.array_equal(img1,img2) == True:
                    print("Timer has stopped, waiting 10 seconds before watchmen terminates.")
                    screenshot_3 = pyautogui.screenshot(region=(700,60, 140, 90))
                    img3 = np.array(screenshot_3)
                    time.sleep(10)
                    screenshot_4 = pyautogui.screenshot(region=(700,60, 140, 90))
                    img4 = np.array(screenshot_4)
                    
                    if np.array_equal(img3,img4) == True:
                        try:
                    
                            location = pyautogui.locateCenterOnScreen(image_path, region=(0,0,1920,1080), confidence=0.7)
                            locationx, locationy = pyautogui.locateCenterOnScreen(image_path, region=(0,0,1920,1080), confidence=0.7)
                            #print(str(locationy))

                            # IF COLLISION IS FOUND
                            if location is not None:
                        
                        
                                pyautogui.moveTo(locationx,locationy-100)
                                pyautogui.dragTo(1600, 50, button='left', duration=2)

                                screenshot = ImageGrab.grab()
                                #Save the screenshot to a file
                                screenshot.save(path + "\\SimulationData_" + str(date_time) + "\\Collision_Screenshots\\Collision_SS-"+ str(number_of_screenshots) + ".png")
                                # Close the screenshot
                                screenshot.close()
                                time.sleep(2)
                                keyboard.press('enter')
                                keyboard.release('enter')
                                print("Collision Detected! -  Image Captured - " + "Collision_SS-"+ str(number_of_screenshots) + ".png")
                                number_of_screenshots = number_of_screenshots + 1
                                time.sleep(2)
                            #IF NO COLLISION IS FOUND
                            else:
                                print("Simulation has stopped! Watchmen terminated!")
                                currentDateAndTime = datetime.now()
                                text_file.write("\nSimulation completed, Time: "+ str(currentDateAndTime) + ", Number of Collisions:  "+ str(number_of_screenshots))
                                text_file.close()
                                break
                                sys.exit()
                                #IF NO COLLISION IS FOUND
                        except:
                            print("Simulation has stopped! Watchmen terminated!")
                            currentDateAndTime = datetime.now()
                            text_file.write("\nSimulation has stopped, Time: "+ str(currentDateAndTime) + ", Number of Collisions:  "+ str(number_of_screenshots))
                            text_file.close()
                            break
                            sys.exit()

            #### COLLISION CHECK 
                try:
                    
                    location = pyautogui.locateCenterOnScreen(image_path, region=(0,0,1920,1080), confidence=0.7)
                    locationx, locationy = pyautogui.locateCenterOnScreen(image_path, region=(0,0,1920,1080), confidence=0.7)
                    #print(str(locationy))

                    # IF COLLISION IS FOUND
                    if location is not None:
                        
                        
                        pyautogui.moveTo(locationx,locationy-100)
                        pyautogui.dragTo(1600, 50, button='left', duration=2)

                        screenshot = ImageGrab.grab()
                        #Save the screenshot to a file
                        screenshot.save(path + "\\SimulationData_" + str(date_time) + "\\Collision_Screenshots\\Collision_SS-"+ str(number_of_screenshots) + ".png")
                        # Close the screenshot
                        screenshot.close()
                        time.sleep(2)
                        keyboard.press('enter')
                        keyboard.release('enter')
                        print("Collision Detected! -  Image Captured - " + "Collision_SS-"+ str(number_of_screenshots) + ".png")
                        number_of_screenshots = number_of_screenshots + 1
                        time.sleep(2)
                    #IF NO COLLISION IS FOUND
                    else:
                        print("..")
                        time.sleep(1)
                #IF NO COLLISION IS FOUND
                except:
                    location = None
                    print(".")
                    
                    screenshot_2 = pyautogui.screenshot(region=(180,60, 140, 90))
                    img2 = np.array(screenshot_2)
                    screenshot_2.save("S:\\CAD_Office\\Muhsin\\NXOPEN\\Simulation_Watchmen_V1\\TIMER_CHECK_DATA\\Timer2-" + username +".png")
                    time.sleep(1)
                    
                program_screenshot2 = pyautogui.screenshot(region=(75,200, 420, 850))
                ps_array2 = np.array(program_screenshot2)
                if np.array_equal(ps_array1,ps_array2) != True:
                    program_screenshot4.save(path + "\\SimulationData_" + str(date_time) + "\\ToolPathTime\\Op_SS-"+ str(program_number) + "-END.png")
                    program_screenshot3 = pyautogui.screenshot(region=(0,0, 520, 1100))
                    time.sleep(1)
                    currentDateAndTime = datetime.now()
                    program_screenshot3.save(path + "\\SimulationData_" + str(date_time) + "\\ToolPathTime\\Op_SS-"+ str(program_number) + "-START.png")
                    text_file.write("\nOperation Change at " + str(currentDateAndTime) + " . Change: " + str(program_number) + " Op_SS-"+ str(program_number) + "-START.png saved!")
                    print("Operation change detected! -  Image Captured - " + "Op_SS-"+ str(program_number))
                    program_number = program_number + 1
                
        #RUN FUNCTION
        capture_collision(image_path)
        
        
        
        #FUNCTION TO PRINT MOUSE POSITION
        #print(str(pyautogui. position()))
if __name__ == '__main__':
    main()