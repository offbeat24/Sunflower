// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from sunflower_interfaces:msg/TfliteResult.idl
// generated code does not contain a copyright notice

#ifndef SUNFLOWER_INTERFACES__MSG__DETAIL__TFLITE_RESULT__FUNCTIONS_H_
#define SUNFLOWER_INTERFACES__MSG__DETAIL__TFLITE_RESULT__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "sunflower_interfaces/msg/rosidl_generator_c__visibility_control.h"

#include "sunflower_interfaces/msg/detail/tflite_result__struct.h"

/// Initialize msg/TfliteResult message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * sunflower_interfaces__msg__TfliteResult
 * )) before or use
 * sunflower_interfaces__msg__TfliteResult__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_sunflower_interfaces
bool
sunflower_interfaces__msg__TfliteResult__init(sunflower_interfaces__msg__TfliteResult * msg);

/// Finalize msg/TfliteResult message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_sunflower_interfaces
void
sunflower_interfaces__msg__TfliteResult__fini(sunflower_interfaces__msg__TfliteResult * msg);

/// Create msg/TfliteResult message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * sunflower_interfaces__msg__TfliteResult__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_sunflower_interfaces
sunflower_interfaces__msg__TfliteResult *
sunflower_interfaces__msg__TfliteResult__create();

/// Destroy msg/TfliteResult message.
/**
 * It calls
 * sunflower_interfaces__msg__TfliteResult__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_sunflower_interfaces
void
sunflower_interfaces__msg__TfliteResult__destroy(sunflower_interfaces__msg__TfliteResult * msg);


/// Initialize array of msg/TfliteResult messages.
/**
 * It allocates the memory for the number of elements and calls
 * sunflower_interfaces__msg__TfliteResult__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_sunflower_interfaces
bool
sunflower_interfaces__msg__TfliteResult__Sequence__init(sunflower_interfaces__msg__TfliteResult__Sequence * array, size_t size);

/// Finalize array of msg/TfliteResult messages.
/**
 * It calls
 * sunflower_interfaces__msg__TfliteResult__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_sunflower_interfaces
void
sunflower_interfaces__msg__TfliteResult__Sequence__fini(sunflower_interfaces__msg__TfliteResult__Sequence * array);

/// Create array of msg/TfliteResult messages.
/**
 * It allocates the memory for the array and calls
 * sunflower_interfaces__msg__TfliteResult__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_sunflower_interfaces
sunflower_interfaces__msg__TfliteResult__Sequence *
sunflower_interfaces__msg__TfliteResult__Sequence__create(size_t size);

/// Destroy array of msg/TfliteResult messages.
/**
 * It calls
 * sunflower_interfaces__msg__TfliteResult__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_sunflower_interfaces
void
sunflower_interfaces__msg__TfliteResult__Sequence__destroy(sunflower_interfaces__msg__TfliteResult__Sequence * array);

#ifdef __cplusplus
}
#endif

#endif  // SUNFLOWER_INTERFACES__MSG__DETAIL__TFLITE_RESULT__FUNCTIONS_H_
