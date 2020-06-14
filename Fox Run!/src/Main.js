class Game {
	constructor() {
		this.clock = null;
	}

	init(status, fox, cactus) {
		this.status = status;
		this.fox = fox;
		this.cactus = cactus;
	}

	run() {
		document.addEventListener('keydown', this.jumpPressed.bind(this));
		document.getElementById("start").onclick = () => {this.b_Press("start")};
		document.getElementById("reset").onclick = () => {this.b_Press("reset")};
		this.clock = setInterval(this.clock_tick.bind(this), 40);
	}

	start() {
		if (this.status.isPaused()) {
			this.status.setPlaying();
		} else {
			this.status.setPaused();
		}
	}

	reset() {
		this.status.setPaused();

		this.cactus.score = 0;
		this.cactus.x = -31;
		this.cactus.through = false;
		this.cactus.opacity = 0;
		document.getElementById('cactus').style.marginLeft = String(this.cactus.x)+'vw';
		document.getElementById('cactus').style.opacity = this.cactus.opacity * 0.1;
		this.cactus.delay = Math.floor(Math.random() * Math.floor(45));

		this.fox.y = 0;
		this.fox.hp = 3;
		this.fox.frame_idx = 1;
		this.fox.hit_stat = false;
		this.fox.inv_stat = false;
		this.fox.des_stat = false;
		this.fox.jump_stat = false;
		document.getElementById('fox').src = "fox/vector/" + this.fox.frame_idx + ".png";
		document.getElementById('fox').style.marginTop = '16vw';

		for (let i=1; i < 4; i++){
			document.getElementById(String(i)).style.visibility = 'visible';
		}
		document.getElementById('start').innerHTML = 'Play';
	}

	clock_tick() {
		let zeroes = 4 - String(this.cactus.score).length;

		document.querySelector(".score").innerHTML = String('0'.repeat(zeroes)) + String(this.cactus.score);

		if (this.fox.hp > 0) {

			if (!(this.fox.isInvincible()) && !(this.fox.isHit()) && this.cactus.x > -77 && this.cactus.x < -66) {
			this.fox.hit(this.status.isPlaying());
			}

			if (!this.status.isPaused()) {
				if (!this.fox.jump_stat){
					this.fox.animate();
				} else {
					this.fox.jump();
				}
				this.cactus.move(this.fox.hit_stat);
			}

		} else {
			this.status.setPaused();
		}
	}



	jumpPressed(event) {
		if (event.keyCode == 32 && !this.fox.isAirborn()){
			this.fox.jump_stat = true;
		}
	}


	b_Press(targ) {
	document.getElementById(targ).classList.add('jello-horizontal');
	setTimeout(() => document.getElementById(targ).classList.remove('jello-horizontal'), 900);
	if (targ != 'reset') {
		if (document.getElementById(targ).innerHTML == 'Play') {
			this.start();
			setTimeout(() => {document.getElementById(targ).innerHTML = 'Pause'}, 900);
		} else {
			this.start();
			setTimeout(() => {document.getElementById(targ).innerHTML = 'Play'}, 900);
		}
	} else {
		this.reset();
		
	}
}

}


window.addEventListener('load', () => {
	const status = new Status();
	const fox = new Fox();
	const game = new Game();
	const cactus = new Cactus();

	game.init(status, fox, cactus);
	game.run();
});



class Status {
	constructor() {
		this.setPaused();
	}

	setPlaying() {
		this.condition = 'playing';
	}

	setPaused() {
		this.condition = 'paused';
	}

	isPlaying() {
		return this.condition === 'playing';
	}

	isPaused() {
		return this.condition === 'paused';
	}

}

class Fox {
	constructor() {
		this.y = 0;

		this.frame_idx = 1; 

		this.hit_stat = false;
		this.inv_stat = false;
		this.des_stat = false;
		this.jump_stat = false;
		this.hp = 3;
	}

	isAirborn() {
		return this.y > 0;
	}

	isJumping() {
		return this.jump_stat;
	}

	/*isDescending() {

	}*/

	isInvincible() {
		return this.inv_stat;
	}

	isHit() {
		return this.hit_stat;
	}

	animate() {
		if (this.frame_idx < 12) {
			this.frame_idx += 1;
		} else {
			this.frame_idx = 1;
		}

		document.getElementById('fox').src = "fox/vector/" + this.frame_idx + ".png";
	}


	jump() {
		if (this.y == 8) {
			this.des_stat =  true;
		}

		if (this.y > 4) {
			this.inv_stat = true;
		} else {
			this.inv_stat = false;
		}


		if (this.y < 8 && !this.des_stat) {
			document.getElementById('fox').style.marginTop = String(16 - this.y) + 'vw';
			this.y += 1;
		} else if (this.y > 0 && this.des_stat) {
			document.getElementById('fox').style.marginTop = String(16 - this.y) + 'vw';
			this.y -= 1;
		}

		if (this.y == 0) {
			this.des_stat = false;
			this.jump_stat = false;
		}


	}

	hit(isrunning) {
		if (!this.hit_stat && isrunning) {
		this.hit_stat = true;
		this.hp -= 1;
		if (this.hp >= 0){
			document.getElementById(String(this.hp + 1)).style.visibility = "hidden";
		}
		document.getElementById("fox").classList.add('blink-1');
		setTimeout(() => document.getElementById("fox").classList.remove('blink-1'), 600);
		setTimeout(() => this.hit_stat = false, 600);
		}
	}
}


class Cactus {
	constructor() {
		this.score = 0;
		this.x = -31;
		this.through = false;
		this.opacity = 0;
		document.getElementById('cactus').style.opacity = this.opacity * 0.1;
		this.delay = Math.floor(Math.random() * Math.floor(45))
	}

	move(hit) {
		if (this.delay <= 0) {
			if (this.x < -71 && !this.through){
				this.through = true;
			}

			if (this.opacity < 10 && !this.through) {
				this.opacity += 1;
				document.getElementById('cactus').style.opacity = this.opacity * 0.1;
			} else if (this.x > -77){
				document.getElementById('cactus').style.marginLeft = String(this.x)+'vw';
				this.x -= 2;
			} else if (this.opacity > 0 && this.through){
				this.opacity -= 2;	
				document.getElementById('cactus').style.opacity = this.opacity * 0.1;
			} else {
				if (!hit){
				this.score += 1;
				}
				this.x = -31;
				this.through = false;
				this.opacity = 0;
				document.getElementById('cactus').style.marginLeft = String(this.x)+'vw';
				document.getElementById('cactus').style.opacity = this.opacity * 0.1;
				this.delay = Math.floor(Math.random() * Math.floor(45));
			}
		} else {
			this.delay -= 1;
		}
}
}