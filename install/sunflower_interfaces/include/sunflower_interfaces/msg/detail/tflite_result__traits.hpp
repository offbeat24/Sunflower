// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from sunflower_interfaces:msg/TfliteResult.idl
// generated code does not contain a copyright notice

#ifndef SUNFLOWER_INTERFACES__MSG__DETAIL__TFLITE_RESULT__TRAITS_HPP_
#define SUNFLOWER_INTERFACES__MSG__DETAIL__TFLITE_RESULT__TRAITS_HPP_

#include "sunflower_interfaces/msg/detail/tflite_result__struct.hpp"
#include <rosidl_runtime_cpp/traits.hpp>
#include <stdint.h>
#include <type_traits>

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<sunflower_interfaces::msg::TfliteResult>()
{
  return "sunflower_interfaces::msg::TfliteResult";
}

template<>
inline const char * name<sunflower_interfaces::msg::TfliteResult>()
{
  return "sunflower_interfaces/msg/TfliteResult";
}

template<>
struct has_fixed_size<sunflower_interfaces::msg::TfliteResult>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<sunflower_interfaces::msg::TfliteResult>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<sunflower_interfaces::msg::TfliteResult>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // SUNFLOWER_INTERFACES__MSG__DETAIL__TFLITE_RESULT__TRAITS_HPP_
