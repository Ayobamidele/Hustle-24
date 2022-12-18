

// var regForm = document.getElementById("reg")
// var orderDetails = document.getElementById("orderDetails")
// var creditCardInput = document.getElementById("id_card_number");
// var loginOpt = document.getElementById("loginOpt");

// function display_register() {
// 	if (user !== 'AnonymousUser') {
// 		regForm.remove()
// 		loginOpt.remove()
// 		orderDetails.classList.remove("col-lg-4")
// 		orderDetails.classList.add("col-lg-12")
// 	}
// }

	
// var disp = display_register();
// var form = document.getElementById('regform')
// $(document).on('click', '#placeOrder', function submitFormData(){
	
// 	var shippingInfo = {
// 		'address':null,
// 		'city':null,
// 		'state':null,
// 		'zipcode':null,
// 		'country':null,
// 		'card_number':null,
// 		'name_on_card':null,
// 		'year':null,
// 		'month':null,
// 		'cvv':null,
// 	}
// 	var userFormData = {
// 		"email":null,
// 	}
// 	if(user == 'AnonymousUser'){
// 		userFormData.email = form.email.value
// 		shippingInfo.address = form.address.value
// 		shippingInfo.city = form.city.value
// 		shippingInfo.state = form.state.value
// 		shippingInfo.zipcode = form.zipcode.value
// 		shippingInfo.country = form.country.value
// 		shippingInfo.card_number = form.card_number.value
// 		shippingInfo.name_on_card = form.name_on_card.value
// 		shippingInfo.month = form.valueAsDate
// 		shippingInfo.year = form.valueAsDate
// 		shippingInfo.cvv = form.cvv.value
// 	}
// 	var url = "/cart/process-order";
// 	fetch(url, {
// 		method :'POST',
// 		headers:{
// 			"Content-Type":"application/json",
// 			"X-CSRFToken":csrftoken,
// 		},
// 		body: JSON.stringify({"form": userFormData.email })
// 	})
// 	.then((response) => response.json())
// 	.then((data) => {
// 		console.log('Success:', data);
// 		alert('Transaction completed');
// 		cart = {}
// 		document.cookie ="cart=" + JSON.stringify(cart) + ";domain=; path=/"
// 		// window.location.href = "{% url 'shop:home' %}"
// 	})
// })

// creditCardInput.onkeydown = function(e) {
// 	var cursor = this.selectionStart;
// 	if (this.selectionEnd != cursor) return;

// 	if (e.which == 46) {
// 		if (this.value[cursor] == " ") this.selectionStart++;
// 	} else if (e.which == 8) {
// 		if (cursor && this.value[cursor - 1] == " ") this.selectionEnd--;
// 	}

// }.oninput = function() {
// 	var value = this.value;
// 	var cursor = this.selectionStart;

// 	var matches = value.substring(0, cursor).match(/[^0-9]/g);

// 	if (matches) cursor -= matches.length;
// 	value = value.replace(/[^0-9]/g, "").substring(0, 24);
// 	var formatted = "";
// 	for (var i=0, n=value.length; i<n; i++) {
// 		if (i && i % 4 == 0) {
// 			if (formatted.length <= cursor) cursor++;
// 			formatted += " ";
// 		}
// 		formatted += value[i];
// 	}
// 	if (formatted == this.value) return;

// 	this.value = formatted;
// 	this.selectionEnd = cursor;
// };