# &lt;Smart_Attendance_System/&gt;
An Attendance system which detracts face and takes attendance. It makes with Python. <br>
<b><h3>developed by <a href="https://devtarak.github.io/" target="_blank">Tarak's Team</a>.</h3></b>
<br>  <h2>Features</h2>
  <ul>
    <li>Detects faces in real-time using the webcam feed.</li>
    <li>Compares the detected faces with known faces to recognize individuals.</li>
    <li>Tracks attendance by matching the recognized faces with a pre-defined list of known faces.</li>
    <li>Records attendance in a CSV file with the format "YYYY-MM-DD.csv", where each row represents an attendance entry.</li>
  </ul>

  <h2>Prerequisites</h2>
  <ul>
    <li>Python 3.x</li>
  </ul>

  <h2>Installation</h2>
  <ol>
    <li>Clone the repository or download the code files.</li>
    <li>Install the required dependencies using the following command:</li>
  </ol>

  <pre><code>pip install -r requirements.txt</code></pre>

  <p>This command will read the <code>requirements.txt</code> file and install the necessary modules (<code>opencv-python</code>, <code>face_recognition</code>, <code>numpy</code>).</p>

  <h2>Usage</h2>
  <ol>
    <li>Place the images of the known individuals in the "photos" directory. Ensure that each image contains only one face.</li>
    <li>Update the <code>known_faces_names</code> list with the names and relevant information of the known individuals.</li>
    <li>Run the script using the following command:</li>
  </ol>

  <pre><code>python main.py</code></pre>

  <p>The webcam feed will open, and faces detected in real-time will be compared with the known faces.</p>

  <p>If a recognized face matches a known face, their attendance will be marked in the CSV file for the current date.</p>

  <p>Press 'q' to stop the program and close the webcam feed.</p>

  <p>The attendance records for each day will be saved in separate CSV files with the format "YYYY-MM-DD.csv".</p>

  <h2>Customization</h2>
  <ul>
    <li>You can modify the code to include additional features or customize the user interface.</li>
    <li>Adjust the window padding, font, font size, and colors according to your preferences.</li>
  </ul>

  <h2>Limitations</h2>
  <ul>
    <li>The accuracy of face recognition depends on the quality of the input images and environmental conditions (lighting, angles, etc.).</li>
    <li>The script assumes that each person's image contains only one face.</li>
    <li>In multi-face scenarios, the script may recognize the most similar face from the known faces.</li>
    <li>Large-scale deployment may require additional optimizations and considerations.</li>
  </ul>

  <h2>License</h2>
  <p>This project is licensed under the <a href="LICENSE">MIT License</a>.</p>

  <h2>Acknowledgments</h2>
  <ul>
    <li>This script was developed based on the <code>face_recognition</code> library by Adam Geitgey.</li>
    <li>The script was created as a demonstration project for educational purposes.</li>
  </ul>

  <p>Feel free to update the README.md file with any additional information or instructions as per your requirements.</p>
