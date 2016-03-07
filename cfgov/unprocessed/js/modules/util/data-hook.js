'use strict';

// Required modules.
var standardType = require( './standard-type' );

/**
 * @param {HTMLNode} element - DOM element.
 * @param {string} value
 *   Value to add to the element's JS data-* hook.
 * @throws {Error} If supplied value contains a space,
 *   which would mean it would be two values, which is likely a typo.
 * @returns {string} The value that was added.
 */
function add( element, value ) {
  if ( value.indexOf( ' ' ) !== -1 ) {
    var msg = standardType.JS_HOOK + 'values cannot contain spaces!';
    throw new Error( msg );
  }

  var values = element.getAttribute( standardType.JS_HOOK );
  if ( values !== null ) {
    value = values + ' ' + value;
  }
  element.setAttribute( standardType.JS_HOOK, value );

  return value;
}

/**
 * @param {HTMLNode} element - DOM element.
 * @param {string} value
 *   Value to remove from the JS data-* hook value.
 * @returns {boolean} True if value was removed, false otherwise.
 */
function remove( element, value ) {
  var values = element.getAttribute( standardType.JS_HOOK );
  var index = values.indexOf( value );
  var values = values.split( ' ' );
  if ( index > -1 ) {
    values.splice( index, 1 );
    element.setAttribute( standardType.JS_HOOK, values.join( ' ' ) );
    return true;
  }

  return false;
}

/**
 * @param {HTMLNode} element - DOM element.
 * @param {string} value
 *   Value to check as existing as a JS data-* hook value.
 * @returns {boolean} True if the data-* hook value exists, false otherwise.
 */
function contains( element, value ) {
  var values = element.getAttribute( standardType.JS_HOOK );
  // If JS data-* hook is not set return immediately.
  if ( !values ) { return false; }
  values = values.split( ' ' );

  return values.indexOf( value ) > -1 ? true : false;
}

module.exports = {
  add:      add,
  contains: contains,
  remove:   remove
};
