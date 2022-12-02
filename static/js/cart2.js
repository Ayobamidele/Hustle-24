// Test
// $(document).ready(function(){
//  alert('worked');
//  // ajax call here
// });

$(document).on('click', '.cart-add', function (e) {
    e.preventDefault();
    product = e.target.dataset['product']
    action = e.target.dataset['action']
    url = cart_url +'/add'
    $.ajax({
      type: 'POST',
      url: url,
      data: {
        id: product,
        action: action,
        csrfmiddlewaretoken: csrftoken,
      },
      success: function (json) {
        document.getElementById("cart-total").innerHTML = json.qty
        document.getElementById("cart-container-total").innerHTML = json.qty
        document.getElementById("total_price").innerHTML = "$" + json.prc

        if (json.updated_quantity !== false) {
          $(e.target).offsetParent().find(".counter-value").val(json.updated_quantity) 
        }


        if (json.total_price !== false) {
          console.log(e)
          $(e.target).offsetParent().offsetParent().offsetParent().find(".cart-item-total-price").text("$" + json.total_price) 
        }

      },
      error: function (xhr, errmsg, err) {}
    });
});

$(document).on('click', '.cart-remove', function (e) {
    e.preventDefault();
    product = e.target.dataset['product']
    action = e.target.dataset['action']
    url = cart_url + "/remove"
    $.ajax({
      type: 'POST',
      url: url,
      data: {
        id: product,
        action: action,
        csrfmiddlewaretoken: csrftoken,
      },
      success: function (json) {
        document.getElementById("cart-total").innerHTML = json.qty
        document.getElementById("cart-container-total").innerHTML = json.qty
        document.getElementById("total_price").innerHTML = "$" + json.prc

        if (json.updated_quantity !== false) {
          $(e.target).offsetParent().find(".counter-value").val(json.updated_quantity) 
        }


        if (json.total_price !== false) {
          $(e.target).offsetParent().offsetParent().offsetParent().find(".cart-item-total-price").text("$" + json.total_price) 
        }

        if (json.removeItem == true) {
          $(e.target).offsetParent().offsetParent().offsetParent().remove() 
        }
      },
      error: function (xhr, errmsg, err) {}
    });
});


$(document).on('click', '.cart-item-close', function (e) {
    e.preventDefault();
    product = e.target.dataset['product']
    action = e.target.dataset['action']
    url = cart_url + "/remove-all"
    $.ajax({
      type: 'POST',
      url: url,
      data: {
        id: product,
        action: action,
        csrfmiddlewaretoken: csrftoken,
      },
      success: function (json) {
        document.getElementById("cart-total").innerHTML = json.qty
        document.getElementById("cart-container-total").innerHTML = json.qty
        document.getElementById("total_price").innerHTML = "$" + json.prc


        $(e.target).offsetParent().remove()
        if (json.qty == 0) {
          $(".cart-item-container").html('<h1 class="mx-auto py-3 pb-3 text-center">Empty</h1>')
        }
      },
      error: function (xhr, errmsg, err) {}
    });
});


$.ajax({
  type: 'POST',
  url: cart_url + "/status",
  data: {
    action: "get_status",
    csrfmiddlewaretoken: csrftoken,
  },
  success: function (json) {
    document.getElementById("cart-total").innerHTML = json.qty
  },
  error: function (xhr, errmsg, err) {}
});


