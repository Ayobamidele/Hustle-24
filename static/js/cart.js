// var updateBtns = document.querySelectorAll('.update-cart');
// var updateWatchlists = document.querySelectorAll('.update-watch-list');
// var cartTotal = document.getElementById("cart-total")

let today = new Date()
let sameDay = new Date(today)

// updateBtns.forEach(updateBtn => updateBtn.addEventListener('click', (e) => {
// 	var productId = updateBtn.dataset.product
// 	var action = updateBtn.dataset.action
// 	console.log('productId:', productId, 'Action:', action)

// 	console.log('User:', user)
// 	if (user == 'AnonymousUser')  {
// 		addCookieItem(productId, action)
// 	} else {
// 		updateUserOrder(productId, action)
// 	}
// 	// location.reload() // chage to update 
// }));


// updateWatchlists.forEach(updateWatchlist => updateWatchlist.addEventListener('click', (e) => {
// 	var productId = updateWatchlist.dataset.product
// 	var action = updateWatchlist.dataset.action
// 	var quantity = updateWatchlist.dataset.quantity
// 	var price = updateWatchlist.dataset.price
// 	var date = sameDay

// 	console.log('productId:', productId, 'Action:', action, updateWatchlist, updateWatchlist.dataset)

// 	console.log('User:', user)
// 	if (user == 'AnonymousUser')  {
// 		addCookieWatchItem(productId, action, quantity, price, date)
// 	} else {
// 		updateUserWatchlist(productId, action, quantity, price, date)
// 	}
// 	updateWatchlist.classList.toggle('text-danger')
// 	e.preventDefault();
// 	updateWatchlist.firstElementChild.classList.toggle('heartBeat')
// 	location.reload()
// }));

// function updateUserOrder(productId, action) {
// 	console.log('User is authenticated, sending data ...')
	
// 	var url = '/cart/update-item'	
// 	event.preventDefault();
// 	fetch(url, {
// 		method:"POST",
// 		headers:{
// 			"Content-Type":"appication/json",
// 			"X-CSRFToken":csrftoken
// 		},
// 		body:JSON.stringify({"productId":productId, "action":action})
// 	})
// 	.then((response) => {
// 		cartTotal.innerHTML = parseInt(cartTotal.innerHTML) + 1;
// 		return response.json();
// 	})
// 	.then((data) => {
// 		console.log('Data:', data)
// 		// location.reload()
// 	})
// }

// function addCookieItem(productId, action) {
// 	console.log('User is not authenticated')	
// 	if (action == 'add'){
// 		if (cart[productId] == undefined){
// 			cart[productId] = {'quantity': 1}
// 		} else {
// 			cart[productId]['quantity'] += 1
// 		}
// 	}
// 	if (action == 'remove'){
// 		cart[productId]['quantity'] -= 1

// 		if (cart[productId]['quantity'] <= 0){
// 			console.log('Item should be deleted')
// 			delete cart[productId];
// 		}
// 	}
// 	if (action == 'removeAll'){
// 		console.log('All Items should be deleted')
// 		delete cart[productId];
// 	}
// 	console.log('Cart:', cart)
// 	document.cookie = 'cart=' + JSON.stringify(cart) + ';domain=;path=/'
// 	location.reload()
// }

// function updateUserWatchlist(productId, action, quantity, price, date) {
// 	console.log('User is authenticated, sending data ...')
	
// 	var url = '/watch_list/update-watch_list'	
// 	event.preventDefault();
// 	fetch(url, {
// 		method:"POST",
// 		headers:{
// 			"Content-Type":"appication/json",
// 			"X-CSRFToken":csrftoken,
// 		},
// 		body:JSON.stringify({
// 			"productId":productId,
// 			"action":action,
// 			'quantity': quantity,
// 			'price': price,
// 			'date': date,
// 		})
// 	})
// 	.then((data) => {
// 		console.log('Data:', data)
// 		// location.reload()
// 	})
// }

// function addCookieWatchItem(productId, action, quantity, price, date) {
// 	console.log('User is not authenticated')	
// 	alert(user)
// 	if (action == "add"){
//   		if (watchlist[productId] == undefined){
// 			watchlist[productId] = {
// 				'quantity': quantity,
// 				'price': price,
// 				'date': date,
// 			}
// 		}
// 	}
// 	else if (action == "remove"){
// 		if (watchlist[productId] != undefined){
// 			delete watchlist[productId];
// 		}
// 	}
// 	console.log('Item ${action}')
// 	console.log('Watch-list:', watchlist)
// 	document.cookie = 'watchlist=' + JSON.stringify(watchlist) + ';domain=;path=/'
// 	// location.reload()
// }


closeSetUpShop.onclick =  function() {
	setUpShop.remove();
	navSetUpShop.classList.toggle("invisible");
	document.cookie = 'shop=true;domain=;path=/'
}
