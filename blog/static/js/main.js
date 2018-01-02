$(document).ready(() => {
  /*
  $('.login-button').on('click', () => {// Clicking login opens login form and hides signup form
    $('.signup-form').hide();
    $('.login-form').toggle();
    //$('.login-button').toggleClass('button-active-login');
    $('html,body').scrollTop(0);

  });

  $('.signup-button').on('click', () => {//Clicking sing up opens sign up forn and hides log in form
    $('.login-form').hide();
    $('.signup-form').toggle();
    //$('.signup-button').toggleClass('button-active-signup');
    $('html,body').scrollTop(0);
  });

  $('#getstarted').on('click', () => {//Clicking Get Started opens sign up forn and hides log in form
    //$('.login-form').hide();
    //$('.signup-form').toggle();
    //$('html,body').scrollTop(0);

  });
  $('#getstarted2').on('click', () => {//Clicking Get Started opens sign up forn and hides log in form
    $('.login-form').hide();
    $('.signup-form').toggle();
    $('html,body').scrollTop(0);
  });

  $(".login-button").click(function(event) {//On small devices, clicking login or signup will collapse the navbar
    if (!$(this).parent().hasClass('dropdown'))
        $(".navbar-collapse").collapse('hide');
  })
  $(".signup-button").click(function(event) {
    if (!$(this).parent().hasClass('dropdown'))
        $(".navbar-collapse").collapse('hide');
  })
*/

    $('.card-btn1').on('click', event => {//LIKE button click funtion
      $(event.currentTarget).toggleClass('active');
    });

    $(".card-btn1").click(function() {
    if ($(this).text() == "Like") {
        $(this).text("Unlike");
    } else {
        $(this).text("Like");
    };
  });


    $('.follow-btn').on('click', event => {//LIKE button click funtion
      $(event.currentTarget).toggleClass('active');
    });

    $(".follow-btn").click(function() {
    if ($(this).text() == "Follow") {
        $(this).text("Following");
    } else {
        $(this).text("Follow");
    };
  });




/*
  $('.card-btn1').on('click', () => {
    if ($(".card-btn1").is(":disabled"))
    {
      $('.card-btn1').prop('disabled', false);
    }
    else if ($(".card-btn1").is(":not(:disabled)"))
    {
      $('.card-btn1').prop('disabled', true);
    }
  })


*/

});
