import React, {useState, useEffect} from 'react'

import './AudioVerify.css'

function AudioVerify() {

  const [recording, setRecording] = useState()
  useEffect(() => {
    var constraints = {
      audio: true,
      //video: false
    };
    async function getMedia(constraints) {
        let stream = null;
        try {
            stream = await navigator.mediaDevices.getUserMedia(constraints);
            // console.log(stream.getAudioTracks()[0].getCapabilities()) ;
            // localVideoref.current.srcObject = stream;
            // localVideoref.current.muted = true;
            audio.src = window.URL.createObjectURL(stream)
            audio.play()
            mediaRecorder = new MediaRecorder(stream)
            chunks = []
            mediaRecorder.ondataavailable = e => {
              if(e.data && e.data.size>0){
                chunks.push(e.data)
              }
            }
        } catch (err) {
            /* handle the error */
            console.log(err);
        }
    }

    getMedia(constraints);
  }, []);
  var localVideoref = React.createRef();

  return (
    <div className="wrapper">

      <header>
        <h1>Web dictaphone</h1>
      </header>

      <section className="main-controls">
        <canvas className="visualizer" height="60px"></canvas>
        <div id="buttons">
          <button className="record">Record</button>
          <button className="stop">Stop</button>
        </div>
      </section>

      <section className="sound-clips">


      </section>

      <video ref={localVideoref} autoPlay ></video>
    </div>
  );
}

export default AudioVerify