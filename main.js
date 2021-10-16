var BASE = 'http://127.0.0.2:5000';

async function host() {
	let response = await fetch(BASE + '/image');
	let result = await response.json();
	console.log(result);
	document.querySelector('#main').src = BASE + result.path;
}

host();