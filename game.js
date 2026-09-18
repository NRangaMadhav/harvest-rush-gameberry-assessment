const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d');
const scoreEl = document.getElementById('score');
const timerEl = document.getElementById('timer');
const statusEl = document.getElementById('status');
const startBtn = document.getElementById('startBtn');

const groundY = canvas.height - 72;
let gameRunning = false;
let score = 0;
let timeLeft = 45;
let lastTime = 0;
let spawnTimer = 0;
let collectibles = [];
let clouds = [];
let keys = {};
let player = {
  x: 130,
  y: groundY - 80,
  width: 42,
  height: 80,
  speed: 4,
  dx: 0,
  dy: 0,
  facing: 1,
  bob: 0
};

function resetGame() {
  score = 0;
  timeLeft = 45;
  collectibles = [];
  clouds = [
    { x: 150, y: 70, w: 90, h: 36 },
    { x: 480, y: 110, w: 120, h: 38 },
    { x: 820, y: 80, w: 110, h: 34 }
  ];
  player.x = 130;
  player.y = groundY - 80;
  player.facing = 1;
  scoreEl.textContent = '0';
  timerEl.textContent = '45';
  statusEl.textContent = 'Collect crops and tools before the timer ends!';
}

function startGame() {
  resetGame();
  gameRunning = true;
  startBtn.textContent = 'Restart Round';
}

function clamp(value, min, max) {
  return Math.min(Math.max(value, min), max);
}

function spawnCollectible() {
  const types = ['carrot', 'tomato', 'water', 'hammer', 'apple'];
  const type = types[Math.floor(Math.random() * types.length)];
  const size = type === 'water' || type === 'hammer' ? 22 : 26;
  collectibles.push({
    type,
    x: 40 + Math.random() * (canvas.width - 120),
    y: 120 + Math.random() * (groundY - 180),
    size,
    angle: Math.random() * Math.PI * 2,
    bob: Math.random() * 100
  });
  if (collectibles.length > 10) collectibles.shift();
}

function updatePlayer() {
  let moveX = 0;
  if (keys['ArrowLeft'] || keys['a']) moveX -= 1;
  if (keys['ArrowRight'] || keys['d']) moveX += 1;
  if (moveX !== 0) player.facing = moveX > 0 ? 1 : -1;
  player.x += moveX * player.speed;
  player.x = clamp(player.x, 20, canvas.width - 80);
  player.y = clamp(player.y, 110, groundY - 70);
  if (keys['ArrowUp'] || keys['w']) player.y -= 4;
  if (keys['ArrowDown'] || keys['s']) player.y += 4;
}

function drawCloud(x, y, w, h) {
  ctx.fillStyle = 'rgba(255,255,255,0.74)';
  ctx.beginPath();
  ctx.arc(x, y, h * 0.65, 0, Math.PI * 2);
  ctx.arc(x + w * 0.28, y - h * 0.1, h * 0.66, 0, Math.PI * 2);
  ctx.arc(x + w * 0.62, y + h * 0.08, h * 0.62, 0, Math.PI * 2);
  ctx.arc(x + w * 0.9, y, h * 0.6, 0, Math.PI * 2);
  ctx.fill();
}

function drawBackground() {
  ctx.fillStyle = '#cfefff';
  ctx.fillRect(0, 0, canvas.width, canvas.height);

  clouds.forEach((cloud) => drawCloud(cloud.x, cloud.y, cloud.w, cloud.h));

  ctx.fillStyle = '#d9f5be';
  ctx.fillRect(0, 250, canvas.width, 240);

  ctx.fillStyle = '#7cc96a';
  ctx.fillRect(0, 420, canvas.width, 120);

  ctx.fillStyle = '#f8d38a';
  ctx.fillRect(0, groundY, canvas.width, canvas.height - groundY);

  for (let i = 0; i < 12; i++) {
    const x = i * 120 + 30;
    ctx.fillStyle = '#8d5a2f';
    ctx.fillRect(x, groundY - 60, 18, 60);
    ctx.fillStyle = '#4bb55d';
    ctx.fillRect(x - 28, groundY - 40, 72, 32);
  }

  ctx.fillStyle = '#9ddf6c';
  ctx.fillRect(0, groundY - 10, canvas.width, 10);
}

function drawCollectible(item) {
  const { type, x, y, size, angle } = item;
  ctx.save();
  ctx.translate(x, y);
  ctx.rotate(angle);

  if (type === 'carrot') {
    ctx.fillStyle = '#ff9f43';
    ctx.beginPath();
    ctx.moveTo(0, -size); ctx.lineTo(size * 0.55, 0); ctx.lineTo(0, size); ctx.lineTo(-size * 0.55, 0); ctx.closePath();
    ctx.fill();
    ctx.fillStyle = '#64b569';
    ctx.fillRect(-6, -size * 0.75, 12, size * 0.55);
  } else if (type === 'tomato') {
    ctx.fillStyle = '#ef5a51';
    ctx.beginPath(); ctx.arc(0, 0, size * 0.72, 0, Math.PI * 2); ctx.fill();
    ctx.fillStyle = '#4fae67';
    ctx.fillRect(-5, -size * 0.8, 10, size * 0.7);
  } else if (type === 'apple') {
    ctx.fillStyle = '#ef5157';
    ctx.beginPath(); ctx.arc(0, 0, size * 0.75, 0, Math.PI * 2); ctx.fill();
    ctx.fillStyle = '#6ab95d';
    ctx.fillRect(-4, -size * 0.9, 8, size * 0.7);
  } else if (type === 'water') {
    ctx.fillStyle = '#6ec8ff';
    ctx.fillRect(-size * 0.55, -size, size * 1.1, size * 2);
    ctx.fillStyle = '#d5f5ff';
    ctx.fillRect(-size * 0.3, -size * 1.4, size * 0.6, size * 0.7);
  } else {
    ctx.fillStyle = '#c7a54a';
    ctx.fillRect(-size * 0.7, -size * 0.5, size * 1.4, size * 1.1);
    ctx.fillStyle = '#8a5d2e';
    ctx.fillRect(-size * 0.2, -size * 1.5, size * 0.4, size * 1.2);
  }

  ctx.restore();
}

function drawPlayer() {
  const { x, y, width, height, facing } = player;
  ctx.save();
  ctx.translate(x + width / 2, y + height / 2);
  ctx.scale(facing, 1);

  ctx.fillStyle = '#52a052';
  ctx.fillRect(-18, -32, 36, 44);
  ctx.fillStyle = '#f2d2a8';
  ctx.fillRect(-16, -56, 32, 26);
  ctx.fillStyle = '#2d4d38';
  ctx.fillRect(-16, -62, 10, 10);
  ctx.fillRect(6, -62, 10, 10);
  ctx.fillStyle = '#f4d37a';
  ctx.fillRect(-18, -8, 12, 36);
  ctx.fillRect(6, -8, 12, 36);
  ctx.fillStyle = '#fdc04d';
  ctx.fillRect(-24, 26, 18, 14);
  ctx.fillRect(6, 26, 18, 14);

  ctx.restore();
}

function checkCollection() {
  collectibles = collectibles.filter((item) => {
    const dx = item.x - (player.x + player.width / 2);
    const dy = item.y - (player.y + player.height / 2);
    const distance = Math.hypot(dx, dy);
    if (distance < 48) {
      score += 10;
      scoreEl.textContent = String(score);
      statusEl.textContent = `Picked up ${item.type}! Keep farming!`;
      return false;
    }
    return true;
  });
}

function update(dt) {
  if (!gameRunning) return;

  timeLeft = Math.max(0, timeLeft - dt / 1000);
  timerEl.textContent = String(Math.ceil(timeLeft));

  if (timeLeft <= 0) {
    gameRunning = false;
    statusEl.textContent = `Round complete! Final score: ${score}`;
    return;
  }

  spawnTimer += dt;
  if (spawnTimer > 1100) {
    spawnTimer = 0;
    spawnCollectible();
  }

  updatePlayer();
  checkCollection();
  clouds.forEach((cloud) => {
    cloud.x -= 0.2;
    if (cloud.x < -150) cloud.x = canvas.width + 80;
  });
}

function render() {
  drawBackground();
  collectibles.forEach((item) => drawCollectible(item));
  drawPlayer();

  ctx.fillStyle = '#103b1f';
  ctx.font = 'bold 22px Segoe UI';
  ctx.fillText('Harvest Rush', 16, 32);
  ctx.fillStyle = '#103b1f';
  ctx.font = '18px Segoe UI';
  ctx.fillText(`Score: ${score}`, 18, 60);
  ctx.fillText(`Time: ${Math.ceil(timeLeft)}`, canvas.width - 110, 60);
}

let lastFrame = 0;
function gameLoop(timestamp) {
  const dt = timestamp - lastFrame;
  lastFrame = timestamp;
  update(dt);
  render();
  requestAnimationFrame(gameLoop);
}

window.addEventListener('keydown', (event) => {
  keys[event.key] = true;
  keys[event.key.toLowerCase()] = true;
  if (event.key === ' ') {
    if (!gameRunning) startGame();
  }
});

window.addEventListener('keyup', (event) => {
  keys[event.key] = false;
  keys[event.key.toLowerCase()] = false;
});

startBtn.addEventListener('click', startGame);
resetGame();
requestAnimationFrame(gameLoop);
