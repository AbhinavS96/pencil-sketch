async function uploadFile() {
	let formData = new FormData();
	formData.append("file", fileupload.files[0]);
	let method = "";
	if (document.querySelector('#pencil-sketch').checked)
		method = "/pencilsketch";
	else if (document.querySelector('#color-sketch').checked)
		method = "/colorpencilsketch"
	let response = await fetch(method, {
		method: "POST",
		body: formData
	});
	console.log(response);
	let result = await response.json();
	console.log(result);
	document.querySelector('#main').src = result.path;
}