async function loadReminders() {
  const res = await fetch('/api/reminders');
  const data = await res.json();
  const list = document.getElementById('list');
  list.innerHTML = '';
  data.forEach(r => {
    const li = document.createElement('li');
    li.textContent = `${r.message} (every ${r.interval_min} min)`;
    list.appendChild(li);
  });
}

document.getElementById('add').onclick = async () => {
  const msg = document.getElementById('msg').value;
  const intv = parseInt(document.getElementById('intv').value);
  await fetch('/api/reminders', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({message: msg, interval_min: intv})
  });
  loadReminders();
};

loadReminders();
