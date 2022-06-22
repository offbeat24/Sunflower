// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from sunflower_interfaces:msg/TfliteResult.idl
// generated code does not contain a copyright notice

#ifndef SUNFLOWER_INTERFACES__MSG__DETAIL__TFLITE_RESULT__BUILDER_HPP_
#define SUNFLOWER_INTERFACES__MSG__DETAIL__TFLITE_RESULT__BUILDER_HPP_

#include "sunflower_interfaces/msg/detail/tflite_result__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace sunflower_interfaces
{

namespace msg
{

namespace builder
{

class Init_TfliteResult_shoulder_r
{
public:
  explicit Init_TfliteResult_shoulder_r(::sunflower_interfaces::msg::TfliteResult & msg)
  : msg_(msg)
  {}
  ::sunflower_interfaces::msg::TfliteResult shoulder_r(::sunflower_interfaces::msg::TfliteResult::_shoulder_r_type arg)
  {
    msg_.shoulder_r = std::move(arg);
    return std::move(msg_);
  }

private:
  ::sunflower_interfaces::msg::TfliteResult msg_;
};

class Init_TfliteResult_shoulder_l
{
public:
  explicit Init_TfliteResult_shoulder_l(::sunflower_interfaces::msg::TfliteResult & msg)
  : msg_(msg)
  {}
  Init_TfliteResult_shoulder_r shoulder_l(::sunflower_interfaces::msg::TfliteResult::_shoulder_l_type arg)
  {
    msg_.shoulder_l = std::move(arg);
    return Init_TfliteResult_shoulder_r(msg_);
  }

private:
  ::sunflower_interfaces::msg::TfliteResult msg_;
};

class Init_TfliteResult_ear_r
{
public:
  explicit Init_TfliteResult_ear_r(::sunflower_interfaces::msg::TfliteResult & msg)
  : msg_(msg)
  {}
  Init_TfliteResult_shoulder_l ear_r(::sunflower_interfaces::msg::TfliteResult::_ear_r_type arg)
  {
    msg_.ear_r = std::move(arg);
    return Init_TfliteResult_shoulder_l(msg_);
  }

private:
  ::sunflower_interfaces::msg::TfliteResult msg_;
};

class Init_TfliteResult_ear_l
{
public:
  explicit Init_TfliteResult_ear_l(::sunflower_interfaces::msg::TfliteResult & msg)
  : msg_(msg)
  {}
  Init_TfliteResult_ear_r ear_l(::sunflower_interfaces::msg::TfliteResult::_ear_l_type arg)
  {
    msg_.ear_l = std::move(arg);
    return Init_TfliteResult_ear_r(msg_);
  }

private:
  ::sunflower_interfaces::msg::TfliteResult msg_;
};

class Init_TfliteResult_eye_r
{
public:
  explicit Init_TfliteResult_eye_r(::sunflower_interfaces::msg::TfliteResult & msg)
  : msg_(msg)
  {}
  Init_TfliteResult_ear_l eye_r(::sunflower_interfaces::msg::TfliteResult::_eye_r_type arg)
  {
    msg_.eye_r = std::move(arg);
    return Init_TfliteResult_ear_l(msg_);
  }

private:
  ::sunflower_interfaces::msg::TfliteResult msg_;
};

class Init_TfliteResult_eye_l
{
public:
  explicit Init_TfliteResult_eye_l(::sunflower_interfaces::msg::TfliteResult & msg)
  : msg_(msg)
  {}
  Init_TfliteResult_eye_r eye_l(::sunflower_interfaces::msg::TfliteResult::_eye_l_type arg)
  {
    msg_.eye_l = std::move(arg);
    return Init_TfliteResult_eye_r(msg_);
  }

private:
  ::sunflower_interfaces::msg::TfliteResult msg_;
};

class Init_TfliteResult_nose
{
public:
  Init_TfliteResult_nose()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_TfliteResult_eye_l nose(::sunflower_interfaces::msg::TfliteResult::_nose_type arg)
  {
    msg_.nose = std::move(arg);
    return Init_TfliteResult_eye_l(msg_);
  }

private:
  ::sunflower_interfaces::msg::TfliteResult msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::sunflower_interfaces::msg::TfliteResult>()
{
  return sunflower_interfaces::msg::builder::Init_TfliteResult_nose();
}

}  // namespace sunflower_interfaces

#endif  // SUNFLOWER_INTERFACES__MSG__DETAIL__TFLITE_RESULT__BUILDER_HPP_
