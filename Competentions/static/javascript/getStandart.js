function getStandart(csrf_token){
  //$("#leftcolumn").append("<p>Hello</p>");
  
  alert('axax is coming');
    $.ajax({
      type: "POST",
      url: "../getStandart/",
      data:  {
        standartTitle: "Программист",
        csrfmiddlewaretoken: csrf_token,
      },
      success: function(msg){
        $(".LeftColumn").append(msg);
      }
    })
    
}