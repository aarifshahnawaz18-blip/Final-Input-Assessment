def clean_data_streams(stream1, stream2):
    cleaned_set = set()   # to store unique valid IDs
    error_log = []        # to store errors

    # merge both streams
    combined_stream = list(stream1) + list(stream2)

    for index, item in enumerate(combined_stream):
        try:
            # check for None
            if item is None:
                raise ValueError("None value found")

            # try casting to integer (handling wrong types)
            value = int(item)

            # add to set (automatically keeps unique values)
            cleaned_set.add(value)

        except Exception as e:
            error_log.append(f"Index {index}: {item} -> {str(e)}")

    return cleaned_set, error_log


# 🔹 Simulated Data Streams (Dirty Data)
stream1 = [1, 2, "3", None, "abc", 5]
stream2 = {4, "6", None, "7x", 2, 8}

# 🔹 Function Call
cleaned_data, errors = clean_data_streams(stream1, stream2)

# 🔹 Output
print("Cleaned Unique Data:", cleaned_data)
print("Error Log:")
for err in errors:
    print(err)