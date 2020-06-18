$(document).ready(function(){
    //contact form 
    var contactForm = $(".contact-form")
    var contactFormMethod = contactForm.attr("method")
    var contactFormEndpoint = contactForm.attr("action") 
    
    function displaySubmitting(submitBtn, defaultText, doSubmit){
        if (doSubmit){
        submitBtn.addClass("disabled")
        submitBtn.html("<i class='fa fa-spin fa-spinner'></i> Sending...")
        } else {
        submitBtn.removeClass("disabled")
        submitBtn.html(defaultText)
        }
        
    }


    contactForm.submit(function(event){
        event.preventDefault()

        var contactFormSubmitBtn = contactForm.find("[type='submit']")
        var contactFormSubmitBtnTxt = contactFormSubmitBtn.text()
        var contactFormData = contactForm.serialize()
        var thisForm = $(this)
        displaySubmitting(contactFormSubmitBtn, "", true)
        $.ajax({
        method: contactFormMethod,
        url:  contactFormEndpoint,
        data: contactFormData,
        success: function(data){
            contactForm[0].reset()
            $.alert({
            title: "Success!",
            content: data.message + ". You will hear from us soon !",
            theme: "modern",
            })
            setTimeout(function(){
            displaySubmitting(contactFormSubmitBtn, contactFormSubmitBtnTxt, false)
            }, 500)
        },
        error: function(error){
            var jsonData = error.responseText
            console.log(jsonData)
            var msg = ""
            $.each(JSON.parse(jsonData), function(key, value){ 
            msg = msg + " Error ("+" Check this ): " + value[0].message + "<br/>";
            })
            $.alert({
            title: "Oops!",
            content: msg ,
            theme: "modern",
            })

            setTimeout(function(){
            displaySubmitting(contactFormSubmitBtn, contactFormSubmitBtnTxt, false)
            }, 500)

        }
        })
    })

    //Search
    var searchForm = $(".search-form")
    var searchInput = searchForm.find("[name = 'q']")
    var typingTimer;
    var typingInterval = 1500
    var searchButton = searchForm.find("[type = 'submit']")
    searchInput.keyup(function(event){
        clearTimeout(typingTimer)
        typingTimer = setTimeout(performSearch, typingInterval)
    })
    searchInput.keydown(function(event){
        clearTimeout(typingTimer)
    })
    function displaySearching(){
        searchButton.addClass("disabled")
        searchButton.html("<i class='fa fa-spin fa-spinner'></i> Searching...")
    }
    function performSearch(){
        displaySearching()
        var query = searchInput.val()
        setTimeout(function(){
        window.location.href = '/search/?q=' + query
        },1500)
        
    }

    var prodForm = $(".form-product-ajax")
    prodForm.submit(function(event){
        event.preventDefault();
        var thisForm = $(this);
        var actionEndPoint = thisForm.attr("data-endpoint");
        var httpMethod = thisForm.attr("method");
        var formData = thisForm.serialize();

        $.ajax({
        url: actionEndPoint,
        method:httpMethod,
        data:formData,
        success:function(data){   
            var submitSpan = thisForm.find(".submit-span")
            if (data.added){
            submitSpan.html("<button type='submit' class='btn btn-dark'><small>Remove</small></button>")
            }
            else{
            submitSpan.html("<button type='submit' class='btn btn-dark'><small>Add to Cart</small></button>")
            }
            var navBarCount = $(".navbar-cart-count");
            navBarCount.text("("+data.cartItemCount+")");
            var currentPath =window.location.href; 
            if (currentPath.indexOf("cart")!=-1){
            refreshCart()
            }
            },
        error:function(errorData){
            $.alert({
            title : "Oops!",
            content :"An error occurred",
            theme:"Modern"}
            )
        }
        })

    })
    function refreshCart(){
        console.log("In cart")
        var cartTable = $(".cart-table")
        var cartBody = cartTable.find(".cart-body")
        var productRows = cartBody.find(".cart-product")
        var currentUrl = window.location.href
        var refreshCartUrl = '/api/cart/';
        var refreshCartMethod = "GET";
        var data = {};
        $.ajax({
        url:refreshCartUrl,
        method:refreshCartMethod,
        data:data,
        success:function(data){
            var hiddenCartItemRemoveForm = $(".cart-item-remove-form")
            if (data.products.length>0){
            productRows.html(" ")  
            i=data.products.length
            $.each(data.products,function(index,value){
                var newCartItemRemove = hiddenCartItemRemoveForm.clone()
                newCartItemRemove.css("display","block")
                newCartItemRemove.find(".cart-item-product-id").val(value.id)
                cartBody.prepend("<tr><th scope=\"row\">"+i+"</th><td> <a style='text-decoration:None;color:black' href='"+value.url+"'>"+value.name+"</a>"+"</td>"+"<td>"+"Rs. "+value.price+"</td>"+"<td>"+newCartItemRemove.html()+"</td>"+"</tr>")
                i--
            })
            cartBody.find(".cart-subtotal").text("Rs. " + data.subtotal)
            cartBody.find(".cart-total").text("Rs. "+data.total + " (Including Taxes)")
            }
            else{
            window.location.href = currentUrl
            }
        },
        error:function(errorData){
            $.alert({
            title : "Oops!",
            content :"An error occurred",
            theme:"Modern"}
            )
        }
        })
    }
    })  
