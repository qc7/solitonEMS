$(document).ready(() => {
    $("#leave_type").change(() => {
        leave_type = document.querySelector('#leave_type').value;

        $.ajax({
            type: 'get',
            url: configuration['leave']['get_no_of_days'],
            data: { 'leave_type': leave_type },
            dataType: 'json',
            success: (data) => {
                if (data.success) {
                    document.querySelector('#no_days').value = data.no_of_days;
                    if (data.leave == "Annual") {
                        document.querySelector('#no_days').readOnly = false;
                    } else {
                        document.querySelector('#no_days').readOnly = true;
                    }
                } else {
                    alert(data.message);
                }

            },

        });
    });

    $("#st_date").change(() => {
        start_date = document.querySelector('#st_date').value;
        no_days = document.querySelector('#no_days').value;

        $.ajax({
            type: 'get',
            url: configuration['leave']['get_end_date'],
            data: { 'startDate': start_date, 'no_of_days': no_days },
            dataType: 'json',
            success: (data) => {
                if (data.success) {
                    document.querySelector('#end_date').value = data.end_date;
                } else {
                    //alert(data.message);
                }

            },

        });
    });

    // $('#types_table tbody').on('click', '.fa', () => {
    //     var rows = $(this).closest("tr");

    //     document.querySelector('#edit_type').value = rows.find('td:eq(1)').text();
    //     document.querySelector('#edit_days').value = rows.find('td:eq(1)').text();
    //     document.querySelector('#edit_desc').value = rows.find('td:eq(2)').text();

    //     var cc = rows.find('td:eq(1)').text();
    //     console.log(cc);
    //     alert(cc);


    // });

    $('#types_table tbody').on('click', '.fa', () => {

        var tableData = $(this).children("td").map(() => {
            return $(this).text();
        }).get();

        var cc = tableData[0];
        console.log(cc);
        alert(cc);


    });

    // $('.fa').click(() => {
    //     var row = $(this).closest('td');

    //     var col = row.parent().children().index(row);

    //     var vv = row.find('.class').val();
    // }); modal_edit_job

    $("#modal_edit_job").on('show.bs.modal', () => {
        var job_title = $(this).data('name');
        alert(job_title);
        $(".modal-body #title_name").val(job_title);
    });


});