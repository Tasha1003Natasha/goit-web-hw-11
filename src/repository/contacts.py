from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import date, timedelta
from src.entity.models import Contact
from src.schemas.contact import ContactSchema, ContactUpdateSchema


async def get_contacts(limit: int, offset: int, query: str | None,
                       db: AsyncSession):
    stmt = select(Contact)

    if query:
        stmt = stmt.where(
            Contact.name.ilike(f"%{query}%") |
            Contact.surname.ilike(f"%{query}%") |
            Contact.email.ilike(f"%{query}%")
        )

    stmt = stmt.offset(offset).limit(limit)

    contacts = await db.execute(stmt)

    return contacts.scalars().all()


async def get_birthdays(
    db: AsyncSession
):
    today = date.today()
    end_date = today + timedelta(days=7)
    stmt = select(Contact)
    result = await db.execute(stmt)
    contacts = result.scalars().all()

    birthdays = []

    for contact in contacts:
        birthday_this_year = contact.birthday.replace(year=today.year)

        if today <= birthday_this_year <= end_date:
            birthdays.append(contact)

    return birthdays


async def get_contact(contact_id: int, db: AsyncSession):
    stmt = select(Contact).filter_by(id=contact_id)
    contact = await db.execute(stmt)
    return contact.scalar_one_or_none()


async def create_contact(body: ContactSchema, db: AsyncSession):
    contact = Contact(**body.model_dump(exclude_unset=True))
    db.add(contact)
    await db.commit()
    await db.refresh(contact)
    return contact


async def update_contact(contact_id: int, body: ContactUpdateSchema, db: AsyncSession):
    stmt = select(Contact).filter_by(id=contact_id)
    result = await db.execute(stmt)
    contact = result.scalar_one_or_none()
    if contact:
        contact.name = body.name
        contact.surname = body.surname
        contact.email = body.email
        contact.phone = body.phone
        contact.birthday = body.birthday
        contact.info = body.info
        await db.commit()
        await db.refresh(contact)
    return contact


async def delete_contact(contact_id: int, db: AsyncSession):
    stmt = select(Contact).filter_by(id=contact_id)
    contact = await db.execute(stmt)
    contact = contact.scalar_one_or_none()
    if contact:
        await db.delete(contact)
        await db.commit()
    return contact
