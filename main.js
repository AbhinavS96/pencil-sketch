async function hello() {
	let response = await fetch('http://127.0.0.1:5000/');
	let result = await response.json();
	console.log(result.key);
}

hello();