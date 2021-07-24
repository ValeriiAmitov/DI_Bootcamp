let a = 2 + 2;

switch (a) {
  case 3:
    alert( 'Too small' );
    break;
  case 4:
    alert( 'Exactly!' ); //This is the correct answer, because we our condition (a) will be "4" and "4" is in case 4, after this block we have a "break" and code is stoping.
    break;
  case 5:
    alert( 'Too large' );
    break;
  default:
    alert( "I don't know such values" );
}
