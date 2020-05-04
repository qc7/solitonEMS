// $(document).ready(() => {
//     $("#st_date").blur(() => {
//         start_date = document.querySelector('#st_date').value;
//         no_days = document.querySelector('#no_days').value;
//         $.ajax({
//             type: 'get',
//             url: configuration['leave']['get_end_date'],
//             data: { 'startDate': start_date, 'no_of_days': no_days },
//             dataType: 'json',
//             success: function(data) {
//                 document.querySelector('#end_date').value = data.end_date;
//             },
//             error: function(error) {
//                 console.log(error);
//             }

//         });
//         console.log(no_days);
//     });
// });
// const leaveCalculator = (leave, startDate) => {
//     e.preventDefault();

//     const datechanged = document.querySelector('#st_date').value;

//     const cleanedLeave = leave.toLowerCase();

//     if (cleanedLeave === 'annual leave') {
//         const no_of_days = document.querySelector('#no_days').value;
//         return moment(startDate, "DD-MM-YYYY").add(no_of_days, 'days').format('MMMM Do YYYY');
//     }

//     if (cleanedLeave === 'maternity leave') {
//         return moment(startDate, "DD-MM-YYYY").add(60, 'days').format('MMMM Do YYYY');
//     }

//     if (cleanedLeave === 'paternity leave') {
//         return moment(startDate, "DD-MM-YYYY").add(6, 'days').format('MMMM Do YYYY');
//     }

//     if (cleanedLeave === 'compassionate leave') {
//         return moment(startDate, "DD-MM-YYYY").add(6, 'days').format('MMMM Do YYYY');
//     }

//     if (cleanedLeave === 'sick leave') {
//         return moment(startDate, "DD-MM-YYYY").add(5, 'days').format('MMMM Do YYYY');
//     }

//     // console.log(leaveCalculator('sick leave', '20.04.2020'));
//     // alert(leaveCalculator('sick leave', '20.04.2020'));

// }