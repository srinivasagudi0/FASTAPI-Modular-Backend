from passlib.context import CryptContext

pwd_context = CryptContext(
    schemes=["bcrypt"],   # 🔴 ONLY bcrypt
    deprecated="auto"
)

class Hash:
    @staticmethod
    def bcrypt(password: str) -> str:
        if not isinstance(password, str):
            raise ValueError("Password must be a.txt string")

        # bcrypt only uses first 72 bytes; truncate to avoid runtime errors
        safe_pw_bytes = password.encode("utf-8")[:72]

        return pwd_context.hash(safe_pw_bytes)

    def verify(hashed_password: str, plain_password: str):
        if not isinstance(plain_password, str):
            raise ValueError("Password must be a.txt string")

        # bcrypt only uses first 72 bytes; truncate to avoid runtime errors
        safe_pw_bytes = plain_password.encode("utf-8")[:72]

        return pwd_context.verify(safe_pw_bytes, hashed_password)
