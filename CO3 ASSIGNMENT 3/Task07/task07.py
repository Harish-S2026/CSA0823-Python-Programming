import random
import re
import time

contacts_a = [
    {"name": "Dr. Ravi", "phone": "+91 98400 12345", "email": "ravi@example.com"},
    {"name": "Meena", "phone": "98765-43210", "email": "meena@example.com"},
    {"name": "Arun", "phone": "", "email": "arun@example.com"}
]
contacts_b = [
    {"name": "ravi kumar", "phone": "9840012345", "email": "rk@example.com"},
    {"name": "Meena", "phone": "+91-9876543210", "email": "meena@example.com"},
    {"name": "Arun", "phone": None, "email": ""}
]

def normalize_phone(phone):
    if not phone:
        return ""
    digits = re.sub(r"\D", "", phone)
    if digits.startswith("91") and len(digits) == 12:
        digits = digits[2:]
    return digits

def normalize_name(name):
    return " ".join(re.findall(r"[a-z]+", (name or "").lower()))

def merge_contacts(*groups):
    merged = {}
    for group in groups:
        for contact in group:
            phone = normalize_phone(contact.get("phone"))
            name = normalize_name(contact.get("name"))
            email = (contact.get("email") or "").strip().lower()
            key = phone if phone else "name:" + name
            if key not in merged:
                merged[key] = {"name": contact.get("name") or "", "numbers": set(), "emails": set(), "names": set()}
            if name:
                merged[key]["names"].add(name)
            if phone:
                merged[key]["numbers"].add(phone)
            if email:
                merged[key]["emails"].add(email)
    return list(merged.values())

def pairwise_duplicate_count(contacts):
    comparisons = 0
    for i in range(len(contacts)):
        for j in range(i + 1, len(contacts)):
            comparisons += 1
            normalize_phone(contacts[i].get("phone")) == normalize_phone(contacts[j].get("phone"))
    return comparisons

def benchmark(count):
    data = [{"name": "Person " + str(i), "phone": str(9000000000 + i), "email": ""} for i in range(count)]
    start = time.perf_counter()
    merge_contacts(data)
    dictionary_time = time.perf_counter() - start
    if count <= 1000:
        start = time.perf_counter()
        pairwise_duplicate_count(data)
        pairwise_time = time.perf_counter() - start
    else:
        pairwise_time = None
    return dictionary_time, pairwise_time

if __name__ == "__main__":
    merged = merge_contacts(contacts_a, contacts_b)
    for contact in merged:
        print(contact)
    print("Small input pairwise comparisons:", pairwise_duplicate_count(contacts_a + contacts_b))
    random.seed(8)
    for size in (1000, 100000):
        print("Benchmark", size, benchmark(size))
