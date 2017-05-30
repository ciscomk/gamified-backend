$(document).ready(function() {

    $('.helpButton').on('click', function() {

        //var user_id = $(this).attr('user_id')
        //var user_money = $(this).attr('user_money')

        req = $.ajax({
            url : '/help',
            type : 'POST',
            //data : { id : user_id }
        });

        req.done(function(data) {

            //$('#moneySection'+user_id).fadeOut(1000).fadeIn(1000);
            //$('#userMoney'+user_id).text(data.user_money);
            $('#moneySection').fadeOut(1000).fadeIn(1000);
            $('#userMoney').text(data.user_money);
            alert("Help is on the way. $5 has been deducted from your account. Do not click the 'HELP' button again until help arrives.");
        });

    });

    $('.finishButton').on('click', function() {

        //var user_id = $(this).attr('user_id')
        //var user_money = $(this).attr('user_money')

        reqFinish = $.ajax({
            url : '/finish',
            type : 'POST',
            //data : { id : user_id }
        });

        reqFinish.done(function() {

            //$('#moneySection'+user_id).fadeOut(1000).fadeIn(1000);
            //$('#userMoney'+user_id).text(data.user_money);
            alert("A proctor is queued up to check your work. Sit back, relax, and wait.");
        });

    });

	setInterval(function() {
		//$("#userMoney{{ user.id }}").load("money");
        //var user_id_interval = $(this).attr('user_id')
        //console.log($(this).attr('user_id'))
        //reqRefresh = $.ajax({
            //url : '/refreshmoney',
            //type : 'GET',
            //data : { id : user_id }
        //});
        $.getJSON("/refreshmoney",
                function(data) {
                    $('#userMoney').text(data.user_money);
                });

        //reqRefresh.done(function(data) {
            //$('#moneySection'+user_id).fadeOut(1000).fadeIn(1000);
            //$('#userMoney'+user_id_interval).text(data.user_money);
            //alert("Help is on the way. $5 has been deducted from your account. Do not click the 'HELP' button again until help arrives.");
        //});
	}, 30000);


});