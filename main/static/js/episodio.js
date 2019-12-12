
var player = document.querySelector('.player');
var video = document.getElementById('video');
var fsButton = document.getElementById('fs');
var btn = document.getElementById("#pause");

fsButton.addEventListener('click', () => {
	if (document.webkitIsFullScreen) {
		player.classList.remove('is-fullscreen');
		document.webkitCancelFullScreen();
		return;
	}
	
	player.classList.add('is-fullscreen');
	player.webkitRequestFullScreen();
});

function pause() {
	if (video.paused) {
	  video.play();
	  btn.innerHTML = "Pause";
	} else {
	  video.pause();
	  btn.innerHTML = "Play";
	}
  }

  
